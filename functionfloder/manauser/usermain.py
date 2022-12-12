from typing import Optional

from fastapi import APIRouter, HTTPException, Cookie, Depends, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

from sqldeal.SQLMAIN import SessionLocal
from .sql import sqlcurd

usermain = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@usermain.get("/manauser/{info}", tags=["manauser"])
async def serchpage(info: str):
    try:
        html_file = open("./frontend/useradmin/" + info, 'rb').read()
        returnsponce = HTMLResponse(content=html_file, status_code=200)
        return returnsponce
    except:
        raise HTTPException(status_code=404)


class usrinfo(BaseModel):
    ptr: str
    info: str


@usermain.post("/getuser", tags=["manauser"])
async def serchuser(usrs: usrinfo, db=Depends(get_db)):
    return JSONResponse(content=jsonable_encoder(sqlcurd.getuser(db, usrs.ptr, usrs.info)))


@usermain.get("/getuser", tags=["manauser"])
async def serchuserget(ptr: str, db=Depends(get_db)):
    return JSONResponse(content=jsonable_encoder(sqlcurd.getuser(db, ptr)))


@usermain.get("/getgroup", tags=["manauser"])
async def sergrpbsc(ptr: str, db=Depends(get_db)):
    t1 = jsonable_encoder(sqlcurd.getgroup(db, ptr))
    return JSONResponse(content=jsonable_encoder(sqlcurd.getgroup(db, ptr)))


@usermain.post("/getgroup", tags=["manauser"])
async def sergrpbscs(usrs: usrinfo, db=Depends(get_db)):
    return JSONResponse(content=jsonable_encoder(sqlcurd.getgroup(db, usrs.ptr, usrs.info)))


@usermain.post("/getallinfo", tags=["manauser"])
async def getallinfo(users_token: Optional[str] = Cookie(None), db=Depends(get_db)):
    return JSONResponse(content=jsonable_encoder(sqlcurd.getalluserinfo(db)))


class addusermod(BaseModel):
    id: str
    names: str
    usr: str
    pwd: str
    factname: str
    grp: str
    mgrp: int
    birthDate: str
    startDate: str
    endDate: str
    email: Optional[str]
    phone: Optional[str]


@usermain.post("/adduser", tags=["manauser"])
async def adduser(users_token: Optional[str] = Cookie(None),
                  id=Form(),
                  names=Form(),
                  usr=Form(),
                  pwd=Form(),
                  email=Form(),
                  phone=Form(),
                  factname=Form(),
                  grp=Form(),
                  mgrp=Form(),
                  birthDate=Form(),
                  startDate=Form(),
                  endDate=Form(),
                  db=Depends(get_db)):
        db_user = sqlcurd.get_uer_token(db, token=users_token)
        if db_user == 0:
            raise HTTPException(detail="验证失败！", status_code=403)
        else:
            if db_user.ACL != 0:
                raise HTTPException(detail="验证失败！", status_code=403)
        from functionfloder.manauser.sql.sqlcurd import adduserdb
        error = adduserdb(id, names, usr, pwd, factname, grp, mgrp, birthDate, startDate, endDate, email, phone, db)
        if error==1:
            raise HTTPException(status_code=455,detail="Error")

        return JSONResponse(content={"code":0},status_code=200)

@usermain.post("/deluser",tags=["manauser"])
async def deluser(id:str,user_token:Optional[str]=Cookie(None),db=Depends(get_db)):
    db_user = sqlcurd.get_uer_token(db, token=user_token)
    if db_user == 0:
        raise HTTPException(detail="验证失败！", status_code=403)
    else:
        if db_user.ACL != 0:
            raise HTTPException(detail="验证失败！", status_code=403)
    from functionfloder.manauser.sql.sqlcurd import deluserdb
    error = deluserdb(id,db)
    if error == 1:
        raise HTTPException(status_code=455, detail="Error")

    return JSONResponse(content={"code": 0}, status_code=200)