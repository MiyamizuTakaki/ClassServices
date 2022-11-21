from fastapi import APIRouter,HTTPException
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder
sources = APIRouter()
@sources.get("/css/{roter}",response_class=HTMLResponse,tags=["sources"])
async def getmeta(roter:str):
    try:
        html_file = open("./frontend/css/"+roter, 'rb').read()
        returnsponce = HTMLResponse(content=html_file, status_code=200,media_type="application/css")
        return returnsponce
    except:
        raise HTTPException(status_code=404)
@sources.get("/js/{file}",response_class=HTMLResponse,tags=["sources"])
async def getinfos(file:str):
    try:
        html_file = open("./frontend/js/"+file, 'rb').read()
        returnsponce = HTMLResponse(content=html_file, status_code=200,media_type="application/css")
        return returnsponce
    except:
        raise HTTPException(status_code=404)
@sources.get("file/{file}",tags=["sources"])
async def getfiles(file:str):
    s =9