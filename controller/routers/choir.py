from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix='/choir', tags=['Choir'])

# create Choir
@router.post('/', response_model=schemas.ChoirRead)
def create_choir(choir: schemas.ChoirCreate, db: Session = Depends(get_db)):
    new_choir = models.Choirs(**choir.dict())
    db.add(new_choir)
    db.commit()
    db.refresh(new_choir)
    return new_choir

# get Choirs
@router.get('/', response_model=list[schemas.ChoirRead])
def get_choirs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    choirs = db.query(models.Choirs).offset(skip).limit(limit).all()
    return choirs

# get Choir
@router.get('/{id}', response_model=schemas.ChoirRead)
def get_choir(id: int, db: Session = Depends(get_db)):
    choir = db.query(models.Choirs).filter(models.Choirs.id == id).first()
    return choir

# update Choir
@router.put('/{id}', response_model=schemas.ChoirRead)
def update_choir(id: int, updated_choir: schemas.ChoirCreate, db: Session = Depends(get_db)):
    choir_query = db.query(models.Choirs).filter(models.Choirs.id == id)
    if choir_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Choir with id: {id} not found')
    choir_query.update(updated_choir.dict(), synchronize_session=False)
    db.commit()
    return choir_query.first()

# delete Choir
@router.delete('/{id}', response_model=schemas.ChoirRead)
def delete_choir(id: int, db: Session = Depends(get_db)):
    choir = db.query(models.Choirs).filter(models.Choirs.id == id)
    if choir.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Choir with id: {id} does not exist")
    choir.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)