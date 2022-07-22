from pydantic import BaseModel

class MembersBase(BaseModel):
    first_name: str
    surname: str
    date_of_birth: str
    gender: str
    contact: str
    email: str
    address: str
    marital_status_id: int
    member_status_id: int
    membership_id: int
    section_id: int

class MembersCreate(MembersBase):
    pass

class MembersRead(MembersBase):
    id: int

    class Config:
        orm_mode = True

class MaritalStatusBase(BaseModel):
    status_name: str

class MaritalStatusCreate(MaritalStatusBase):
    pass

class MaritalStatusRead(MaritalStatusBase):
    id: int

    class Config:
        orm_mode = True

class MemberStatusBase(BaseModel):
    status_name: str

class MemberStatusCreate(MemberStatusBase):
    pass

class MemberStatusRead(MemberStatusBase):
    id: int

    class Config:
        orm_mode = True

class MembershipStatusBase(BaseModel):
    status_name: str

class MembershipStatusCreate(MembershipStatusBase):
    pass

class MembershipStatusRead(MembershipStatusBase):
    id: int

    class Config:
        orm_mode = True

class ServicesBase(BaseModel):
    date: str
    preacher: str
    litegist_1: str
    litegist_2: str
    choir: str
    preaching_topic: str
    preaching_verses: str

class ServicesCreate(ServicesBase):
    pass

class ServicesRead(ServicesBase):
    id: int

    class Config:
        orm_mode = True

class SectionsBase(BaseModel):
    section_number: int
    area: str
    section_leader: str
    vice_section_leader: str
    treasurer: str
    number_of_families: str

class SectionsCreate(SectionsBase):
    pass

class SectionsRead(SectionsBase):
    id: int

    class Config:
        orm_mode = True

class UsersBase(BaseModel):
    username: str
    password: str
    member_id: int

class UsersCreate(UsersBase):
    pass

class UsersRead(UsersBase):
    id: int

    class Config:
        orm_mode = True

class GuestsBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    gender: str
    email: str
    contact: str
    address: str
    church: str

class GuestsCreate(GuestsBase):
    pass

class GuestsRead(GuestsBase):
    id: int

    class Config:
        orm_mode = True

class ChoirBase(BaseModel):
    choir_name: str
    church: str

class ChoirCreate(ChoirBase):
    pass

class ChoirRead(ChoirBase):
    id: int

    class Config:
        orm_mode = True