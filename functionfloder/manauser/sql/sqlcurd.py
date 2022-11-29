from typing import Optional

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
    dicts={
        "grpnum":info.grpnum,
        "facname":info.Faculy,
        "clsname":info.facname,
        "nckname":info.antrname,
        "statdate":info.statime,
        "enddate":info.endtime
    }
def getgroup(db: Session, ptr: str, info=Optional[str]):
    db_user_firsts = None
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