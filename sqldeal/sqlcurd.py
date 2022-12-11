import logging

from sqlalchemy.orm import Session

from . import SQLORM


def get_user(db: Session, usernames: str):
    return db.query(SQLORM.UserList).filter(SQLORM.UserList.usernames == usernames).first()


def set_user_token(db: Session, usernames: str, token: str):
    try:
        db_user = get_user(db, usernames=usernames)
        db_user.token = token
        db.commit()
        db.refresh(db_user)
    except TypeError:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s"
        )

        ch.setFormatter(formatter)
        logger.addHandler(ch)


def get_uer_token(db: Session, token: str):
    db_user = db.query(SQLORM.UserList).filter(SQLORM.UserList.token == token).first()
    if db_user is not None:
        ust = db_user.usernames
        return {"code": 1, "user": ust}
    else:
        return {"code": 0, "user": "None"}


def get_user_real(db: Session, token: str):
    db_user = db.query(SQLORM.UserList).filter(SQLORM.UserList.token == token).first()
    user_id = ""
    if db_user is not None:
        user_id = db_user.id
    else:
        return {"code": 0, "user": "None"}
    db_real = db.query(SQLORM.RealUser).filter(SQLORM.RealUser.id == user_id).first()
    if db_real is not None:
        return {"code": 1,
                "id": db_real.id,
                "name": db_real.name,
                "groups": db_real.groups,
                "Bachelor": db_real.Bachelor,
                "Faculty": db_real.Faculty,
                "birthdate": db_real.birthdate,
                "startstudy": db_real.startstudy,
                "endstudy": db_real.endstudy,
                "student_status": db_real.student_status,
                "email": db_real.email,
                "telephone": db_real.telephone}
    else:
        return {"code": 0, "user": "None"}
