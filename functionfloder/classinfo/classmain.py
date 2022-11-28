from fastapi import APIRouter, HTTPException, Cookie, Depends, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from sqldeal.SQLMAIN import SessionLocal
from .sql.sqlcurd import *
from pydantic import BaseModel

import json

course = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@course.post("/getcourse", tags=["courses"])
async def getcoursein(users_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    getjson = {}
    i = 0
    getinfos = getcourse(db, users_token)
    for getinfo in getinfos:
        getjson[i] = getinfo
        i = i + 1
    return JSONResponse(content=jsonable_encoder(getjson), status_code=200)


@course.post("/Nowcourse", tags=["courses"])
async def nowcourse(users_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    return JSONResponse(content=nowcoursesql(db, users_token), status_code=200)


@course.post("/advsrch", tags=["courses"])
async def advsrch(grps: str = Form(...), mgrp: int = Form(...), date: int = Form(...), week: int = Form(...),
                  db: Session = Depends(get_db)):
    try:
        if date != 8:
            date = date + 1
        else:
            date = 0
        return JSONResponse(content=jsonable_encoder(advancesearch(db, grps, mgrp, date, week)), status_code=200)
    except:
        raise HTTPException(status_code=404)


@course.post("/grpinfo", tags=["courses"])
async def grpinfo(grps: str, db: Session = Depends(get_db)):
    try:
        return JSONResponse(content=jsonable_encoder(get_groupinfo(db, grps)), status_code=200)
    except:
        raise HTTPException(status_code=404)
class Item(BaseModel):
    info: str
    tip: str
@course.post("/avssimp/", tags=["courses"])
async def avssimp(item:Item, db: Session = Depends(get_db)):
    # try:
        isd = get_moreinfo(db, item.info, item.tip)
        if isd is not None:
            return JSONResponse(content=jsonable_encoder(isd), status_code=200)
        else:
            err = {"code":1}
            return JSONResponse(content=jsonable_encoder(err), status_code=200)
    # except:
    #     raise HTTPException(status_code=404)
