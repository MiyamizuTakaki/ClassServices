from sqlalchemy import Column, Integer, String

from .SQLMAIN import Base


class UserList(Base):  ##用户基础数据
    __tablename__ = "UserList"
    id = Column(String, unique=True, primary_key=True)
    usernames = Column(String, unique=True)
    passwords = Column(String)
    ACL = Column(Integer)
    mgroup = Column(String)
    groups = Column(String)
    token = Column(String)
    token_days = Column(Integer)
    tokenstart = Column(Integer)


class GroupList(Base):
    __tablename__ = "GroupList"
    grpnum = Column(String(100), unique=True, primary_key=True)
    Faculy = Column(String(100))
    facname = Column(String(100), unique=True)
    antrname = Column(String(100))
    statime = Column(String)
    endtime = Column(String)
    studnum = Column(String)


class ACL_List(Base):
    __tablename__ = "ACL_List"
    numbers = Column(Integer, unique=True, primary_key=True)
    names = Column(String(100), unique=True)
    superuser = Column(Integer)
    monitor = Column(Integer)
    class_schc = Column(Integer)
    exam = Column(Integer)
    file = Column(Integer)
    terminal = Column(Integer)


class course(Base):
    __tablename__ = "course"
    groupint = Column(String)
    numbers = Column(Integer, unique=True, primary_key=True)
    days = Column(Integer)
    names = Column(String(100))
    starttime = Column(String(100))
    endtime = Column(String(100))
    weeks = Column(String(100))
    teacher = Column(String)
    address = Column(String)
    expiretime = Column(String)
    types = Column(String)
    mgroup = Column(Integer)


class file(Base):
    __tablename__ = "file"
    numbers = Column(Integer, unique=True, primary_key=True)
    groupint = Column(Integer)
    user_id = Column(Integer, unique=True)
    acl = Column(Integer)
    path = Column(String)


class RealUser(Base):
    __tablename__ = "RealUser"
    id = Column(String(20), unique=True, primary_key=True)
    name = Column(String)
    groups = Column(String)
    mgroup = Column(Integer)
    Bachelor = Column(String)
    Faculty = Column(String)
    birthdate = Column(String)
    startstudy = Column(String)
    endstudy = Column(String)
    student_status = Column(String)
    email = Column(String)
    telephone = Column(String)


class examine(Base):
    __tablename__ = "exam"
    numbers = Column(Integer, unique=True, primary_key=True)
    grp_numbers = Column(Integer)
    mgroup = Column(Integer)
    stattime = Column(String)
    endtime = Column(String)
    settime = Column(String)
    names = Column(String)
    tittle = Column(String)
    sources = Column(Integer)
    all_souces = Column(Integer)
    answer_type = Column(Integer)
    answer_choo = Column(String)
    answer_true = Column(String)
    answer_false = Column(Integer)
    sprise = Column(Integer)
    finishstu = Column(String)
    num = Column(Integer)
