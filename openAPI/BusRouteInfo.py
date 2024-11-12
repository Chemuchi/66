import json

import requests
from key import *
from openAPI.XMLtoJSON import *

'''
66번이 거쳐가는 정류장을 순서대로 출력
"비래동 종점 -> 판암역 종점 -> 비래동 종점" 순으로 출력

필터링 단어는 필요시 추가
'''
url = f"http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getStaionByRoute?busRouteId={routeId_66()}&serviceKey={servicekey()}"
response = requests.get(url)
#print(response.text)


def filterd_busRoute():
    url = f"http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getStaionByRoute?busRouteId={routeId_66()}&serviceKey={servicekey()}"
    response = requests.get(url)

    # 필요한 키들만 필터링
    filter_word = ["BUSSTOP_NM", "BUSSTOP_SEQ", "BUS_NODE_ID", "TOTAL_DIST"]
    filtered_json = filtering(response.content, filter_word)


    return filtered_json

#print(json.dumps(filterd_busRoute(), ensure_ascii=False, indent=4))
#print(convert(response.content))




