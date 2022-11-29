from fastapi import FastAPI, HTTPException, Form, Cookie, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional
from sqldeal import sqlcurd, SQLORM, sqlpydantic
from sqldeal.SQLMAIN import SessionLocal, engine
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from roterdepender import manageinfo, cssjs
from functionfloder.classinfo import classmain
from functionfloder.manauser import usermain
app = FastAPI()
app.include_router(manageinfo.app1)
app.include_router(cssjs.sources)
app.include_router(classmain.course)
from functionfloder.userinfo import users
app.include_router(usermain.usermain)
app.include_router(users.usersmain)


class UserLogin(BaseModel):
    user: str
    passwd: str
    allowautologin: bool

    class Config:
        orm_mode = True


class UserLoginSucess(BaseModel):
    detail: str

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# SQLORM.Base.metadata.create_all(bind=engine)
@app.get("/", response_class=HTMLResponse)
async def root():
    html_file = open("./frontend/index.html", 'rb').read()
    returnsponce = HTMLResponse(content=html_file, status_code=200)
    return returnsponce


@app.get("/cookie")
async def cookietest(users_id: Optional[str] = Cookie(None)):
    return {"name": users_id}


import random
import string
import time


@app.post("/cookiess")
async def autologin(users_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    db_user = sqlcurd.get_uer_token(db, token=users_token)
    returnsponce = JSONResponse(content=db_user, status_code=200)
    return returnsponce


@app.post("/")
async def login(uname: str = Form(...), pswd: str = Form(...), db: Session = Depends(get_db)):
    html_file = open("./frontend/index.html", 'rb').read()

    db_user = sqlcurd.get_user(db, usernames=uname)
    if db_user is None:
        jsons = {"code": 1, "detail": "密码错误"}
        returnsponce = JSONResponse(content=jsonable_encoder(jsons), status_code=200)
        return returnsponce
        # raise HTTPException(status_code=401)
    if db_user.passwords != pswd:
        jsons = {"code": 1, "detail": "密码错误"}
        returnsponce = JSONResponse(content=jsonable_encoder(jsons), status_code=200)
        return returnsponce
    token = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    times = time.time()
    jsons = {"code": 0, "detail": db_user.usernames}
    sqlcurd.set_user_token(db, usernames=uname, token=token)
    returnsponce = JSONResponse(content=jsonable_encoder(jsons), status_code=200)
    ##returnsponce.set_cookie(key="users_token", value=token,expires=5400)
    returnsponce.set_cookie(key="users_token", value=token, expires=9999999)
    return returnsponce
    ##return {"usr": uname,"pwd":pswd}


# crud.py==sqlcurd.py
# database.py==SQLMAIN.py
# main.py==SQLMAIN.py
# models.py==SQLORM.py
# schemas.py==sqlpydantic.py
# SQLORM.Base.metadata.create_all(bind=engine)
@app.get("/{roter}", response_class=HTMLResponse)
async def findhtml(roter: str):
    try:
        if roter == "exit":
            html_file = open("./frontend/index.html" + 'rb').read()
            returnsponce = HTMLResponse(content=html_file, status_code=200)
            returnsponce.set_cookie("users_token", "")
            return returnsponce
        else:
            html_file = open("./frontend/" + roter, 'rb').read()
            returnsponce = HTMLResponse(content=html_file, status_code=200)
            return returnsponce
    except:
        raise HTTPException(status_code=404)


@app.post("/infos")
async def loginset(users_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
    db_user = sqlcurd.get_user_real(db, token=users_token)
    if db_user["code"] == 1:
        return JSONResponse(content=jsonable_encoder(db_user), status_code=200)
    else:
        raise HTTPException(status_code=401)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
