from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix='/guests', tags=['Guests'])

# create Guest
@router.post('/', response_model=schemas.GuestsRead)
def create_guest(guest: schemas.GuestsCreate, db: Session = Depends(get_db)):
    new_guest = models.Guests(**guest.dict())
    db.add(new_guest)
    db.commit()
    db.refresh(new_guest)
    return new_guest

# get Guests
@router.get('/', response_model=list[schemas.GuestsRead])
def get_guests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    guests = db.query(models.Guests).offset(skip).limit(limit).all()
    return guests

# get Guest
@router.get('/{id}', response_model=schemas.GuestsRead)
def get_guest(id: int, db: Session = Depends(get_db)):
    guest = db.query(models.Guests).filter(models.Guests.id == id).first()
    return guest

# update Guest
@router.put('/{id}', response_model=schemas.GuestsRead)
def update_guest(id: int, updated_guest: schemas.GuestsCreate, db: Session = Depends(get_db)):
    guest_query = db.query(models.Guests).filter(models.Guests.id == id)
    if guest_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Guest with id: {id} not found')
    guest_query.update(updated_guest.dict(), synchronize_session=False)
    db.commit()
    return guest_query.first()

# delete Guest
@router.delete('/{id}', response_model=schemas.GuestsRead)
def delete_guest(id: int, db: Session = Depends(get_db)):
    guest = db.query(models.Guests).filter(models.Guests.id == id)
    if guest.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Guest with id: {id} does not exist")
    guest.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)