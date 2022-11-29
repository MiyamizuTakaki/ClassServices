from fastapi import APIRouter, HTTPException, Cookie, Depends, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from sqldeal.SQLMAIN import SessionLocal
from pydantic import BaseModel
from .sql import sqlcurd
usermain = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@usermain.get("/manauser/{info}",tags=["manauser"])
async def serchpage(info:str):
    try:
        html_file = open("./frontend/useradmin/" + info, 'rb').read()
        returnsponce = HTMLResponse(content=html_file, status_code=200)
        return returnsponce
    except:
        raise HTTPException(status_code=404)
class usrinfo(BaseModel):
    ptr:str
    info:str
@usermain.post("/getuser",tags=["manauser"])
async def serchuser(usrs:usrinfo,db = Depends(get_db)):
    return  JSONResponse(content=jsonable_encoder(sqlcurd.getuser(db,usrs.ptr,usrs.info)))
@usermain.get("/getuser",tags=["manauser"])
async def serchuserget(ptr:str,db = Depends(get_db)):
    return  JSONResponse(content=jsonable_encoder(sqlcurd.getuser(db,ptr)))
@usermain.get("/getgroup",tags=["manauser"])
async def sergrpbsc(ptr:str,db=Depends(get_db)):
    return JSONResponse(content=jsonable_encoder(sqlcurd.getgroup(db, ptr)))
@usermain.post("/getgroup",tags=["manauser"])
async def sergrpbscs(usrs:usrinfo,db = Depends(get_db)):
    return  JSONResponse(content=jsonable_encoder(sqlcurd.getgroup(db,usrs.ptr,usrs.info)))