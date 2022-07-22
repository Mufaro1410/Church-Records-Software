from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix='/marital', tags=['Marital Status'])

# create Marial Status
@router.post('/', response_model=schemas.MaritalStatusRead)
def create_marital_status(marital_status: schemas.MaritalStatusCreate, db: Session = Depends(get_db)):
    new_marital_status = models.maritalStatus(**marital_status.dict())
    db.add(new_marital_status)
    db.commit()
    db.refresh(new_marital_status)
    return new_marital_status

# get Marital Statuses
@router.get('/', response_model=list[schemas.MaritalStatusRead])
def get_marital_statuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    marital_statuses = db.query(models.maritalStatus).offset(skip).limit(limit).all()
    return marital_statuses

# get Marital Status
@router.get('/{id}', response_model=schemas.MaritalStatusRead)
def get_marital_status(id: int, db: Session = Depends(get_db)):
    marital_status = db.query(models.maritalStatus).filter(models.maritalStatus.id == id).first()
    return marital_status

# update Marital Status
@router.put('/{id}', response_model=schemas.MaritalStatusRead)
def update_marital_status(id: int, updated_marital_status: schemas.MaritalStatusCreate, db: Session = Depends(get_db)):
    marital_status_query = db.query(models.maritalStatus).filter(models.maritalStatus.id == id)
    if marital_status_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Marital Status with id: {id} not found')
    marital_status_query.update(updated_marital_status.dict(), synchronize_session=False)
    db.commit()
    return marital_status_query.first()

# delete Marital Status
@router.delete('/{id}', response_model=schemas.MaritalStatusRead)
def delete_marital_status(id: int, db: Session = Depends(get_db)):
    marital_status_query = db.query(models.maritalStatus).filter(models.maritalStatus.id == id)
    if marital_status_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Marital Status with id: {id} does not exist")
    marital_status_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)