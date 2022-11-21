from fastapi import APIRouter,HTTPException
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder
app1 = APIRouter()

@app1.get("/school/firstinfo/{index}",tags=["school"])
async def read_user(index: str):
    try:
        html_file = open("./frontend/firstinfo/"+index, 'rb').read()
        returnsponce = HTMLResponse(content=html_file, status_code=200)
        return returnsponce
    except:
        raise HTTPException(status_code=404)
@app1.get("/school/{index}",tags=["school"])
async def read_user(index: str):
    try:
        html_file = open("./frontend/"+index, 'rb').read()
        returnsponce = HTMLResponse(content=html_file, status_code=200)
        return returnsponce
    except:
        raise HTTPException(status_code=404)
@app1.get("/school/schooltest/{index}",tags=["school"])
async def read_user(index: str):
    try:
        html_file = open("./frontend/schooltest/"+index, 'rb').read()
        returnsponce = HTMLResponse(content=html_file, status_code=200)
        return returnsponce
    except:
        raise HTTPException(status_code=404)
@app1.get("/school/myclass/{index}",tags=["school"])
async def read_user(index: str):
    try:
        html_file = open("./frontend/myclass/"+index, 'rb').read()
        returnsponce = HTMLResponse(content=html_file, status_code=200)
        return returnsponce
    except:
        raise HTTPException(status_code=404)
@app1.get("/school/commute/{index}",tags=["school"])
async def read_user(index: str):
    try:
        html_file = open("./frontend/commute/"+index, 'rb').read()
        returnsponce = HTMLResponse(content=html_file, status_code=200)
        return returnsponce
    except:
        raise HTTPException(status_code=404)