from pydantic import BaseModel


class UserList(BaseModel):
    id: str
    usernames: str
    passwords: str
    ACL: int

    class Config:
        orm_mode = True


class Usertoken(UserList):
    token: str
    token_days: int
    tokenstart: int

    class Config:
        orm_mode = True
