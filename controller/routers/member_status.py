from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix='/memberstatus', tags=['Members'])

# create Member
@router.post('/', response_model=schemas.MembersRead)
def create_member(member: schemas.MembersCreate, db: Session = Depends(get_db)):
    new_member = models.Members(**member.dict())
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member

# get Members
@router.get('/', response_model=list[schemas.MembersRead])
def get_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    members = db.query(models.Members).offset(skip).limit(limit).all()
    return members

# get Member
@router.get('/{id}', response_model=schemas.MembersRead)
def get_member(id: int, db: Session = Depends(get_db)):
    member = db.query(models.Members).filter(models.Members.id == id).first()
    return member

# update Member
@router.put('/{id}', response_model=schemas.MembersRead)
def update_member(id: int, updated_member: schemas.MembersCreate, db: Session = Depends(get_db)):
    member_query = db.query(models.Members).filter(models.Members.id == id)
    if member_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Member with id: {id} not found')
    member_query.update(updated_member.dict(), synchronize_session=False)
    db.commit()
    return member_query.first()

# delete Member
@router.delete('/{id}', response_model=schemas.MembersRead)
def delete_member(id: int, db: Session = Depends(get_db)):
    member_query = db.query(models.Members).filter(models.Members.id == id)
    if member_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Member with id: {id} does not exist")
    member_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)