from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix='/services', tags=['Services'])

# create Service
@router.post('/', response_model=schemas.ServicesRead)
def create_service(service: schemas.ServicesCreate, db: Session = Depends(get_db)):
    new_service = models.Services(**service.dict())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

# get Services
@router.get('/', response_model=list[schemas.ServicesRead])
def get_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    services = db.query(models.Services).offset(skip).limit(limit).all()
    return services

# get Service
@router.get('/{id}', response_model=schemas.ServicesRead)
def get_service(id: int, db: Session = Depends(get_db)):
    service = db.query(models.Services).filter(models.Services.id == id).first()
    return service

# update Service
@router.put('/{id}', response_model=schemas.ServicesRead)
def update_service(id: int, updated_service: schemas.ServicesCreate, db: Session = Depends(get_db)):
    service_query = db.query(models.Services).filter(models.Services.id == id)
    if service_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Service with id: {id} not found')
    service_query.update(updated_service.dict(), synchronize_session=False)
    db.commit()
    return service_query.first()

# delete Service
@router.delete('/{id}', response_model=schemas.ServicesRead)
def delete_service(id: int, db: Session = Depends(get_db)):
    service = db.query(models.Services).filter(models.Services.id == id)
    if service.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Service with id: {id} does not exist")
    service.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)