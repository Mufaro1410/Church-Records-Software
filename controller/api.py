from fastapi import FastAPI

from . import models
from controller.routers import members, services, sections, users, guests, marital_status, member_status, membership_status, choir
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(members.router)
app.include_router(marital_status.router)
app.include_router(member_status.router)
app.include_router(membership_status.router)
app.include_router(services.router)
app.include_router(sections.router)
app.include_router(users.router)
app.include_router(guests.router)
app.include_router(choir.router)