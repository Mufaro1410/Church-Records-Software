from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix='/sections', tags=['Sections'])

# create Section
@router.post('/', response_model=schemas.SectionsRead)
def create_section(section: schemas.SectionsCreate, db: Session = Depends(get_db)):
    new_section = models.Sections(**section.dict())
    db.add(new_section)
    db.commit()
    db.refresh(new_section)
    return new_section

# get Sections
@router.get('/', response_model=list[schemas.SectionsRead])
def get_sections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sections = db.query(models.Sections).offset(skip).limit(limit).all()
    return sections

# get Section
@router.get('/{id}', response_model=schemas.SectionsRead)
def get_section(id: int, db: Session = Depends(get_db)):
    section = db.query(models.Sections).filter(models.Sections.id == id).first()
    return section

# update Section
@router.put('/{id}', response_model=schemas.SectionsRead)
def update_section(id: int, updated_section: schemas.SectionsCreate, db: Session = Depends(get_db)):
    section_query = db.query(models.Sections).filter(models.Sections.id == id)
    if section_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Section with id: {id} not found')
    section_query.update(updated_section.dict(), synchronize_session=False)
    db.commit()
    return section_query.first()

# delete Section
@router.delete('/{id}', response_model=schemas.SectionsRead)
def delete_section(id: int, db: Session = Depends(get_db)):
    section = db.query(models.Sections).filter(models.Sections.id == id)
    if section.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Section with id: {id} does not exist")
    section.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)