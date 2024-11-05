
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data.schedule import *
from collections import OrderedDict
app = FastAPI()


@app.get("/")
async def root():
    response_data = OrderedDict([
        ("다음 비래동에서 출발시간", next_birae_time()),
        ("이전 비래동에서 출발시간", previous_birae_time()),
        ("다음 판암역에서 출발시간", next_panam_time()),
        ("이전 판암역에서 출발시간", previous_panam_time())
    ])

    headers = {
        "Cache-Control": "no-control",
        "Pragma": "no-cache"
    }
    return JSONResponse(content=response_data, headers=headers);
