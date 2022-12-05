from sqlalchemy import and_
from sqlalchemy.orm import Session

from sqldeal import SQLORM
from ..sql import modelset

def infobasic(info):
    dicts = {
        "grp_numbers": info.numbers,
        "mgroup": info.mgroup,
        "stattime": info.stattime,
        "endtime": info.endtime,
        "settime": info.settime,
        "names": info.names,
        "all_souces": info.all_souces
    }
    return dicts


def testinfo(info):
    dicts = {
        "name": info.names,
        "num": info.num,
        "answer_type": info.answer_type,
        "title": info.tittle,
        "answer_choo": info.answer_choo
    }
    return dicts


def gettest_stud_basic(db: Session, id: str):
    user_info = db.query(SQLORM.UserList).filter(SQLORM.UserList.id == id).first()
    infos = []
    grps = user_info.group.split(",")
    mgrps = user_info.mgroup.split(",")
    for grp, mgrp in zip(grps, mgrps):
        test_info_basic = db.query(SQLORM.examine).filter(and_(SQLORM.examine.grp_numbers == grp,
                                                               SQLORM.examine.mgroup == mgrp,
                                                               SQLORM.examine.finishstu != user_info.id,
                                                               SQLORM.examine.num == 1)) \
            .order_by(SQLORM.examine.num).all()
        for test_info_basici in test_info_basic:
            infos.append(infobasic(test_info_basici))
    return infos


def gettest_stud_test(db: Session, id: str, number: int):
    user_info = db.query(SQLORM.UserList).filter(SQLORM.UserList.id == id).first()
    infos = []
    grps = user_info.group.split(",")
    mgrps = user_info.mgroup.split(",")
    for grp, mgrp in zip(grps, mgrps):
        test_info_basic = db.query(SQLORM.examine).filter(and_(SQLORM.examine.grp_numbers == grp,
                                                               SQLORM.examine.mgroup == mgrp,
                                                               SQLORM.examine.finishstu != user_info.id,
                                                               SQLORM.examine.number == number)) \
            .order_by(SQLORM.examine.num.desc()).all()
        for test_info_basici in test_info_basic:
            infos.append(testinfo(test_info_basici))
    return infos


def set_stud_test(db: Session, test: modelset.testMod, info: modelset.infoMod):
    numbers = info.numbers
    statime = info.statime
    endtime = info.endtime
    settime = info.settime
    name = info.name
    group = info.grp_numbers
    mgroup = info.mgroup
    sources = info.sources
    db.add(SQLORM.examine(numbers=numbers, grp_numbers=group, mgroup=mgroup, stattime=statime, endtime=endtime,
                          settime=settime, names=name, tittle=test.title, sources=sources, all_souces=sources * 10,
                          answer_type=test.answer_type, answer_choo=(str)(test.answer_choo),
                          answer_true=(str)(test.answer_true),
                          answer_false=0, sprise=0, num=test.num))
    db.commit()
