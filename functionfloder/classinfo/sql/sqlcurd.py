from sqlalchemy.orm import Session
import logging
from sqldeal import SQLORM
from fastapi.encoders import jsonable_encoder
import json
from fastapi import Depends
import time
import datetime
from datetime import timedelta

from sqlalchemy import and_, or_


def infosdict(info):
    dicts = {
        "numbers": info.numbers,
        "days": info.days,
        "groupint": info.groupint,
        "mgroup": info.mgroup,
        "names": info.names,
        "starttime": info.starttime,
        "endtime": info.endtime,
        "weeks": info.weeks,
        "teacher": info.teacher,
        "address": info.address,
        "expiretime": info.expiretime,
        "type": info.types
    }
    return dicts

def getcourse(db: Session, token: str):
    db_user = db.query(SQLORM.UserList).filter(SQLORM.UserList.token == token).first()
    if db_user is not None:
        db_grp = db.query(SQLORM.RealUser).filter(SQLORM.RealUser.id == db_user.id).first()
        groupnumbers = db_grp.groups.split()
        classinfo = []
        for groupnumber in groupnumbers:
            infos = db.query(SQLORM.course).filter(SQLORM.course.groupint == groupnumber).all()
            for info in infos:
                classinfo.append(infosdict(info))
        return classinfo

def nowcoursesql(db: Session, token: str):
    times = time.strftime("%H:%M:%S", time.localtime())
    date = time.strftime("%Y-%m-%d", time.localtime())
    day = time.strftime("%w", time.localtime())
    day1 = int(day)
    sureodd = (int(time.time() / 60 / 60 / 24 / 365 / 7) % 2 + 1)
    db_user = db.query(SQLORM.UserList).filter(SQLORM.UserList.token == token).first()
    db_grp = db.query(SQLORM.RealUser).filter(SQLORM.RealUser.id == db_user.id).first()
    groupnumbers = db_grp.groups.split()
    ftimes = time.strptime(times, "%H:%M:%S")
    strtime = times.split(":")
    dtimes = datetime.timedelta(hours=int(strtime[0]), minutes=int(strtime[1]), seconds=int(strtime[2]))
    fday = time.strptime(day, "%w")
    for groupnumber in groupnumbers:
        infos = db.query(SQLORM.course).filter(SQLORM.course.groupint == groupnumber).all()
        for info in infos:
            if day1 == (info.days) and (sureodd == info.weeks or info.weeks == 0):
                if dtimes > info.starttime:
                    return {"status": 0, "info": json.dumps(infosdict(info), default=str)}
    if time.strptime(day, "%w") > time.strptime("6", "%w"):
        return {"status": 2, "code": 0}
    return {"status": 2, "code": 1}

def advancesearch(db: Session, grps: str, mgrp: int, date: int, week: int):
    reninfo ={}
    i =0
    grpss = grps.split(",")
    for grp in grpss:
        if week == 0:
            getwek = None
        else:
            getwek = week
        if date == 8:
            getday = None
        else:
            getday = date
        infos = db.query(SQLORM.course).filter(
            SQLORM.course.groupint == grp, SQLORM.course.mgroup == mgrp,
                 SQLORM.course.days == getday,SQLORM.course.weeks == 0, SQLORM.course.weeks.in_([0,getwek])).order_by(SQLORM.course.starttime).all()
        for info in infos:
            reninfo[i]= infosdict(info)
            i =i+1
    return reninfo
def get_groupinfo(db:Session,grp:str):
    db_user = db.query(SQLORM.GroupList).filter(SQLORM.GroupList.grpnum == grp).first()
    return {"grpnum":db_user.grpnum,
            "Faculy":db_user.Faculy,
            "facname":db_user.facname,
            "antrname":db_user.antrname,
            "studnum":db_user.studnum}
def get_moreinfo(db:Session,info:str,tip:str):
    if tip=="grp":
        db_user = db.query(SQLORM.GroupList).filter(SQLORM.GroupList.grpnum.like(info+'%')).order_by(SQLORM.GroupList.desc()).all()
        if db_user is not None:
            get ={}
            i=0
            for dbs in db_user:
                get[i]=dbs.grpnum
            return get
    elif tip=="mgrp":
        db_user = db.query(SQLORM.GroupList).filter(SQLORM.GroupList.grpnum == info).first()
        if db_user is not None:
            return int(db_user.studnum)
    return None