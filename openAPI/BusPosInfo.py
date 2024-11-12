from openAPI.BusRouteInfo import *


'''
DIR - 
    0 : 비래동 종점 -> 판암역 종점
    1 : 판암역 종점 -> 비래동 종점
'''
"""url = f"http://openapitraffic.daejeon.go.kr/api/rest/busposinfo/getBusPosByRtid?busRouteId={routeId_66()}&serviceKey={servicekey()}"
response = requests.get(url)
print (response.text)"""

# API 접근이 불가능해 컨테이너가 실행안됨
"""def busPosInfo():
    url = f"http://openapitraffic.daejeon.go.kr/api/rest/busposinfo/getBusPosByRtid?busRouteId={routeId_66()}&serviceKey={servicekey()}"
    response = requests.get(url)
    filtered_data = filtering(response.content, ["BUS_NODE_ID","DIR"])
    return filtered_data



# 노선 정보와 현재 위치 정보를 병합하는 함수
def added_busPosInfo():
    # 66번 버스 노선 정보
    data_with_names = filterd_busRoute()
    if data_with_names is None or "msgBody" not in data_with_names or "itemList" not in data_with_names["msgBody"]:
        return {"error": "Failed to retrieve bus route information"}

    # 현재 버스 위치 정보
    data_to_update = busPosInfo()
    if data_to_update is None or "msgBody" not in data_to_update or "itemList" not in data_to_update["msgBody"]:
        return {"error": "Failed to retrieve bus position information"}

    # 첫 번째 JSON의 BUS_NODE_ID를 기준으로 BUSSTOP_NM과 TOTAL_DIST 매핑
    bus_stop_info_map = {}
    for item in data_with_names["msgBody"]["itemList"]:
        bus_node_id = item.get("BUS_NODE_ID")
        total_dist = int(item.get("TOTAL_DIST", 0) or 0)  # 기본값 0 설정

        if bus_node_id:
            if bus_node_id not in bus_stop_info_map:
                bus_stop_info_map[bus_node_id] = {"BUSSTOP_NM": item.get("BUSSTOP_NM", ""), "TOTAL_DIST": total_dist}
            else:
                # DIR 조건에 따른 TOTAL_DIST 처리 (작은 거리, 큰 거리)
                if total_dist < bus_stop_info_map[bus_node_id]["TOTAL_DIST"]:
                    bus_stop_info_map[bus_node_id]["DIR_0"] = total_dist
                else:
                    bus_stop_info_map[bus_node_id]["DIR_1"] = total_dist

    # 두 번째 JSON 데이터에 BUSSTOP_NM과 TOTAL_DIST 추가
    for item in data_to_update["msgBody"]["itemList"]:
        bus_node_id = item.get("BUS_NODE_ID")
        dir_value = item.get("DIR")

        if bus_node_id in bus_stop_info_map:
            item["BUSSTOP_NM"] = bus_stop_info_map[bus_node_id]["BUSSTOP_NM"]
            # DIR 값에 따라 TOTAL_DIST를 추가
            if dir_value == "0" and "DIR_0" in bus_stop_info_map[bus_node_id]:
                item["TOTAL_DIST"] = bus_stop_info_map[bus_node_id]["DIR_0"]
            elif dir_value == "1" and "DIR_1" in bus_stop_info_map[bus_node_id]:
                item["TOTAL_DIST"] = bus_stop_info_map[bus_node_id]["DIR_1"]
            else:
                item["TOTAL_DIST"] = bus_stop_info_map[bus_node_id]["TOTAL_DIST"]

    return data_to_update



# 함수 실행 및 결과 출력
updated_data = added_busPosInfo()"""

# 최종 결과 출력
#print(json.dumps(updated_data, ensure_ascii=False, indent=4))
"""
{
    "msgHeader": {},
    "msgBody": {
        "itemList": [
            {
                "BUS_NODE_ID": "8002689",
                "DIR": "0",
                "BUSSTOP_NM": "천동주공아파트",
                "TOTAL_DIST": 14032
            },
            {
                "BUS_NODE_ID": "8001400",
                "DIR": "0",
                "BUSSTOP_NM": "대전보건대학",
                "TOTAL_DIST": 1938
            },
            {
                "BUS_NODE_ID": "8005988",
                "DIR": "1",
                "BUSSTOP_NM": "대전대학교동문",
                "TOTAL_DIST": 19044
            }
        ]
    }
}
"""


