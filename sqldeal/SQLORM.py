import pydantic

from .SQLMAIN import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
class UserList(Base):##用户基础数据
    __tablename__ = "UserList"
    id = Column(String,unique =True,primary_key=True)
    usernames = Column(String, unique=True)
    passwords = Column(String)
    ACL = Column(Integer)
    token = Column(String)
    token_days = Column(Integer)
    tokenstart = Column(Integer)
    mgroup = Column(Integer)

class GroupList(Base):
    __tablename__ = "GroupList"
    grpnum = Column(String(100),unique=True,primary_key=True)
    Faculy = Column(String(100))
    facname = Column(String(100),unique=True)
    antrname = Column(String(100))
    statime = Column(String)
    endtime = Column(String)
    studnum = Column(String)

class ACL_List(Base):
    __tablename__="ACL_List"
    numbers = Column(Integer,unique=True,primary_key=True)
    names = Column(String(100),unique=True)
    superuser = Column(Integer)
    monitor = Column(Integer)
    class_schc = Column(Integer)
    exam = Column(Integer)
    file = Column(Integer)
    terminal = Column(Integer)

class course(Base):
    __tablename__="course"
    groupint = Column(String)
    numbers = Column(Integer,unique = True,primary_key=True)
    days = Column(Integer)
    names =Column(String(100))
    starttime =Column(String(100))
    endtime = Column(String(100))
    weeks = Column(String(100))
    teacher = Column(String)
    address = Column(String)
    expiretime = Column(String)
    types = Column(String)
    mgroup = Column(Integer)

class file(Base):
    __tablename__="file"
    numbers = Column(Integer,unique = True,primary_key=True)
    groupint = Column(Integer)
    user_id = Column(Integer,unique = True)
    acl = Column(Integer)
    path = Column(String)

class RealUser(Base):
    __tablename__="RealUser"
    id = Column(String(20),unique = True,primary_key=True)
    name = Column(String)
    groups = Column(String)
    Bachelor = Column(String)
    Faculty = Column(String)
    birthdate = Column(String)
    startstudy = Column(String)
    endstudy = Column(String)
    student_status = Column(String)
    email = Column(String)
    telephone = Column(String)