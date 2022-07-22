from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix='/users', tags=['Users'])

# create User
@router.post('/', response_model=schemas.UsersRead)
def create_user(user: schemas.UsersCreate, db: Session = Depends(get_db)):
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get Users
@router.get('/', response_model=list[schemas.UsersRead])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.Users).offset(skip).limit(limit).all()
    return users

# get User
@router.get('/{id}', response_model=schemas.UsersRead)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    return user

# update User
@router.put('/{id}', response_model=schemas.UsersRead)
def update_user(id: int, updated_user: schemas.UsersCreate, db: Session = Depends(get_db)):
    user_query = db.query(models.Users).filter(models.Users.id == id)
    if user_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id: {id} not found')
    user_query.update(updated_user.dict(), synchronize_session=False)
    db.commit()
    return user_query.first()

# delete User
@router.delete('/{id}', response_model=schemas.UsersRead)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id)
    if user.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)