
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data.schedule import *
from collections import OrderedDict
from openAPI.Arrive import *
app = FastAPI()


@app.get("/")
async def root():
    response_data = OrderedDict([
        ("현재 시간", current_time_str()),
        ("다음 비래동에서 출발시간", next_birae_time()),
        ("이전 비래동에서 출발시간", previous_birae_time()),
        ("다음 판암역에서 출발시간", next_panam_time()),
        ("이전 판암역에서 출발시간", previous_panam_time())
    ])

    headers = {
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache",
        "Expires": "0"
    }
    return JSONResponse(content=response_data, headers=headers, media_type="application/json; charset=utf-8")

@app.get("/nextbirae")
async def from_birae():
    return next_birae_time()
@app.get("/secondnextbirae")
async def second_from_birae():
    return second_next_birae_time()

@app.get("/nextpanam")
async def from_panam():
    return next_panam_time()

@app.get("/secondnextpanam")
async def second_from_panam():
    return second_next_panam_time()

@app.get("/prebirae")
async def pre_birae():
    return previous_birae_time()

@app.get("/prepanam")
async def pre_panam():
    return previous_panam_time()

@app.get("/current")
async def current():
    return current_time_str()

"""@app.get("/fromhome")
async def from_home():
    return check_bus_position_dir_0()

@app.get("/fromschool")
async def from_school():
    return check_bus_position_dir_1()"""
