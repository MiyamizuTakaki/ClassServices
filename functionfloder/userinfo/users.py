from typing import Optional

from fastapi import APIRouter, HTTPException, Depends, Cookie
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from sqldeal import sqlcurd
from sqldeal.SQLMAIN import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


usersmain = APIRouter()


@usersmain.post("/userinfo/main", tags=["usersinfo"])
async def get_info(users_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    try:
        db_user = sqlcurd.get_user_real(db, token=users_token)
        returnsponce = JSONResponse(content=jsonable_encoder(db_user), status_code=200)
        return returnsponce
    except:
        raise HTTPException(status_code=404)
