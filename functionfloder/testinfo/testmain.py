from fastapi import APIRouter, HTTPException, Cookie, Depends, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from sqldeal.SQLMAIN import SessionLocal
from sqldeal.sqlcurd import get_user,get_uer_token
from .sql import sqlcurd
from pydantic import BaseModel
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
testinfo = APIRouter()
@testinfo.get("/testinfo/{info}")
async def getinfo(info:str):
    try:
        html_file = open("./frontend/schooltest/" + info, 'rb').read()
        returnsponce = HTMLResponse(content=html_file, status_code=200)
        return returnsponce
    except:
        raise HTTPException(status_code=404)
@testinfo.post("/testget")
async def gettest(cookie :str=Optional[Cookie], db=Depends(get_db)):
    user_info_more = None
    user_info = get_uer_token(db,cookie)
    if user_info["code"]==1:
        user_info_more = get_user(db,user_info["user"])
@testinfo.post("/starttest")
async def testinfos(number:int,cookie :str=Optional[Cookie], db=Depends(get_db)):
    user_info_more = None
    user_info = get_uer_token(db, cookie)
    if user_info["code"] == 1:
        user_info_more = get_user(db, user_info["user"])
        gets = sqlcurd.gettest_stud_test(db,user_info_more.id,number)
        if gets is not None:
            return JSONResponse(content=jsonable_encoder(sqlcurd.gettest_stud_test(db,user_info_more.id,number)),status_code=200)
        else:
            raise HTTPException(status_code=404)
    else:
        raise HTTPException(status_code=401)