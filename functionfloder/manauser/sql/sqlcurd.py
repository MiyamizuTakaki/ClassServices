from typing import Optional

from pydantic import BaseModel
from sqlalchemy.orm import Session

from sqldeal import SQLORM


def infosdict(info, nickname):
    dicts = {
        "id": info.id,
        "name": info.name,
        "nickname": nickname,
        "facid": info.groups,
        "mfacid": info.mgroup,
        "price": info.Bachelor,
        "fakt": info.Faculty,
        "date": info.birthdate,
        "phone": info.telephone,
        "email": info.email,
        "ststu": info.startstudy,
        "endstu": info.endstudy
    }
    return dicts


def alluser(info):
    return {
        "grpnum": info.grpnum,
        "Faculy": info.Faculy,
        "facname": info.facname,
        "antrname": info.antrname,
        "ststime": info.statime,
        "enddtime": info.endtime,
        "studnum": info.studnum
    }


def getuser(db: Session, ptr: str, info=Optional[str]):
    db_user_firsts = None
    get = []
    if ptr == "-1":
        db_user_firsts = db.query(SQLORM.UserList).order_by(SQLORM.UserList.id.desc()).all()
        db_user_seconds = db.query(SQLORM.RealUser).order_by(SQLORM.RealUser.id.desc()).all()
        for db_user_first, db_user_second in zip(db_user_firsts, db_user_seconds):
            nickname = db_user_first.usernames
            get.append(infosdict(db_user_second, nickname))
    else:
        if ptr == "0":
            db_user_firsts = db.query(SQLORM.RealUser).filter(SQLORM.RealUser.name == info).order_by(
                SQLORM.RealUser.id.desc()).all()
        elif ptr == "1":
            db_user_firsts = db.query(SQLORM.RealUser).filter(SQLORM.RealUser.id == info).order_by(
                SQLORM.RealUser.id.desc()).all()
        elif ptr == "2":
            db_user_firsts = db.query(SQLORM.RealUser).filter(SQLORM.RealUser.birthdate == info).order_by(
                SQLORM.RealUser.id.desc()).all()
        elif ptr == "3":
            db_user_firsts = db.query(SQLORM.RealUser).filter(SQLORM.RealUser.groups == info).order_by(
                SQLORM.RealUser.id.desc()).all()
        elif ptr == "4":
            db_user_firsts = db.query(SQLORM.RealUser).filter(SQLORM.RealUser.Faculty == info).order_by(
                SQLORM.RealUser.id.desc()).all()
        ##db_user_seconds = db.query(SQLORM.RealUser).filter(SQLORM.UserList.id==db_user_firsts).order_by(SQLORM.RealUser.id.desc()).all()
        for db_user_first in db_user_firsts:
            db_user_seconds = db.query(SQLORM.UserList).filter(SQLORM.UserList.id == db_user_first.id).order_by(
                SQLORM.UserList.id.desc()).all()
            for db_user_second in db_user_seconds:
                get.append(infosdict(db_user_first, db_user_second.usernames))
    return get


def infogrp(info):
    dicts = {
        "grpnum": info.grpnum,
        "facname": info.Faculy,
        "clsname": info.facname,
        "nckname": info.antrname,
        "statdate": info.statime,
        "enddate": info.endtime
    }
    return dicts


def getgroup(db: Session, ptr: str, info=Optional[str]):
    global db_user_firsts
    get = []
    if ptr == "-1":
        db_user_firsts = db.query(SQLORM.GroupList).order_by(SQLORM.GroupList.grpnum.desc()).all()
    elif ptr == "0":
        db_user_firsts = db.query(SQLORM.GroupList).filter(SQLORM.GroupList.grpnum == info).order_by(
            SQLORM.GroupList.grpnum.desc()).all()
    elif ptr == "1":
        db_user_firsts = db.query(SQLORM.GroupList).filter(SQLORM.GroupList.Faculy == info).order_by(
            SQLORM.GroupList.grpnum.desc()).all()
    elif ptr == "2":
        db_user_firsts = db.query(SQLORM.GroupList).filter(SQLORM.GroupList.facname == info).order_by(
            SQLORM.GroupList.grpnum.desc()).all()
    elif ptr == "3":
        db_user_firsts = db.query(SQLORM.GroupList).filter(SQLORM.GroupList.antrname == info).order_by(
            SQLORM.GroupList.grpnum.desc()).all()
    elif ptr == "4":
        db_user_firsts = db.query(SQLORM.GroupList).filter(SQLORM.GroupList.statime == info).order_by(
            SQLORM.GroupList.grpnum.desc()).all()
    elif ptr == "5":
        db_user_firsts = db.query(SQLORM.GroupList).filter(SQLORM.GroupList.endtime == info).order_by(
            SQLORM.GroupList.grpnum.desc()).all()
    for db_user_first in db_user_firsts:
        get.append(infogrp(db_user_first))
    return get


def getalluserinfo(db: Session):
    infos = []
    allinfos = db.query(SQLORM.GroupList).order_by(SQLORM.GroupList.grpnum.desc()).all()
    for allinfo in allinfos:
        infos.append(alluser(allinfo))
    return infos


def get_uer_token(db: Session, token: str):
    db_user = db.query(SQLORM.UserList).filter(SQLORM.UserList.token == token).first()
    if db_user is not None:
        ust = db_user.usernames
        return db_user
    else:
        return 0


class addusermod(BaseModel):
    id: str
    names: str
    usr: str
    pwd: str
    email: Optional[str] = None
    phone: Optional[str] = None
    factname: str
    grp: str
    mgrp: int
    birthDate: str
    startDate: str
    endDate: str


def adduserdb(id: str,
              names: str,
              usr: str,
              pwd: str,
              factname: str,
              grp: str,
              mgrp: int,
              birthDate: str,
              startDate: str,
              endDate: str,
              email: Optional[str],
              phone: Optional[str], db: Session):
        grpif = db.query(SQLORM.GroupList).filter(SQLORM.GroupList.grpnum == grp).first()
        add_user = SQLORM.RealUser(id=id, name=names, groups=grp, mgroup=mgrp,
                                   Bachelor=factname, Faculty=grpif.facname, birthdate=birthDate,
                                   startstudy=startDate, endstudy=endDate, email=email, telephone=phone,student_status="3")
        db.add(add_user)
        add_usinfo = SQLORM.UserList(id=id, usernames=usr, passwords=pwd, ACL=1, mgroup=str(mgrp), groups=grp)
        db.add(add_usinfo)
        db.commit()
        return 0

def deluserdb(id:str,db:Session):
    try:
        db.query(SQLORM.RealUser).filter(SQLORM.RealUser.id==id).delete()
        db.commit()
        return 0
    except:
        return 1

def usereditget(id:str,db:Session):
    try:
        db_user1 = db.query(SQLORM.RealUser).filter(SQLORM.RealUser.id==id).first()
        db_user2 = db.query(SQLORM.UserList).filter(SQLORM.UserList.id==id).first()
        return 0
    except:
        return 1