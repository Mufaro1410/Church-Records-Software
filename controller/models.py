from enum import unique
from requests import delete
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Time
from sqlalchemy.orm import relationship

from .database import Base

class Members(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    date_of_birth = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    contact = Column(String, unique=True)
    email = Column(String, unique=True)
    address = Column(String)
    marital_status_id = Column(Integer, ForeignKey('marital_status.id'), nullable=False)
    member_status_id = Column(Integer, ForeignKey('member_status.id'), nullable=False)
    membership_id = Column(Integer, ForeignKey('membership_status.id'), nullable=False)
    section_id = Column(Integer, ForeignKey('sections.id'), nullable=False)

    marital_status = relationship('maritalStatus', back_populates='members')
    member_status = relationship('memberStatus', back_populates='members')
    membership_status = relationship('membershipStatus', back_populates='members')
    #sections = relationship('Sections', back_populates='members')
    users = relationship('Users', back_populates='members')


class maritalStatus(Base):
    __tablename__ = 'marital_status'

    id = Column(Integer, primary_key=True)
    status_name = Column(String, nullable=False, unique=True)

    members = relationship('Members', back_populates='marital_status')

class memberStatus(Base):
    __tablename__ = 'member_status'

    id = Column(Integer, primary_key=True)
    status_name = Column(String, nullable=False, unique=True)

    members = relationship('Members', back_populates='member_status')


class membershipStatus(Base):
    __tablename__ = 'membership_status'

    id = Column(Integer, primary_key=True)
    status_name = Column(String, nullable=False, unique=True)

    members = relationship('Members', back_populates='membership_status')

class Services(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    preacher = Column(Integer, nullable=False)
    litegist_1 = Column(String, nullable=False)
    litegist_2 = Column(String, nullable=False)
    choir = Column(String, nullable=False)
    preaching_topic = Column(String, nullable=False)
    preaching_verses = Column(Integer, nullable=False)

class Sections(Base):
    __tablename__ = 'sections'

    id = Column(Integer, primary_key=True)
    section_number = Column(String, nullable=False)
    area = Column(String, nullable=False)
    section_leader_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    vice_section_leader_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    treasurer_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    number_of_families = Column(String, unique=True)

    #members = relationship('Members')
    section_leader = relationship("Members", foreign_keys=[section_leader_id])
    vice_section_leader = relationship("Members", foreign_keys=[vice_section_leader_id])
    treasurer = relationship("Members", foreign_keys=[treasurer_id])

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    member_id = Column(Integer, ForeignKey('members.id'))
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    members = relationship('Members', back_populates='users')

class Guests(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(String)
    gender = Column(String, nullable=False)
    contact = Column(String)
    email = Column(String)
    address = Column(String)
    church = Column(String)
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    #user_credentials = relationship('UserCredentials', back_populates='users')

class Choirs(Base):
    __tablename__ = 'choirs'

    id = Column(Integer, primary_key=True)
    name: Column(String, unique=True)
    church: Column(String)