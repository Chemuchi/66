
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data.schedule import *
from collections import OrderedDict
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
