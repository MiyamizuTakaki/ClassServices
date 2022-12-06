from sqlalchemy import and_
from sqlalchemy.orm import Session

from sqldeal import SQLORM

def alluser(info):
    return {
        "grpnum":info.grpnum,
        "Faculy":info.Faculy,
        "facname":info.facname,
        "antrname":info.antrname,
        "ststime":info.statime,
        "enddtime":info.endtime
    }

def getalluserinfo(db:Session):
    infos = []
    allinfos = db.query(SQLORM.GroupList).order_by(SQLORM.GroupList.grpnum.desc()).all()
    for allinfo in allinfos:
        infos.append(alluser(allinfo))
    return infos