import json

from .BusPosInfo import busPosInfo
from .BusRouteInfo import filterd_busRoute
# 관심 정류장 이름 목록
dir_0_stations_names = ["효촌마을아파트", "복합터미널", "동부네거리", "가양중학교입구", "한신휴플러스", "삼호아파트"]
dir_1_stations_names = ["판암역", "판암동성당", "용운국제수영장", "복음아파트", "새울", "대전대학교", "대전대학교동문"]

# 버스 위치 정보에 정류장 이름을 추가하는 함수
def added_busPosInfo():
    data_with_names = filterd_busRoute()  # BUSSTOP_NM, BUSSTOP_SEQ, BUS_NODE_ID, TOTAL_DIST 포함된 정류장 정보
    data_to_update = busPosInfo()         # 현재 버스 위치 정보

    # 정류장 정보를 매핑하여 이름을 추가
    bus_stop_name_map = {item["BUS_NODE_ID"]: item for item in data_with_names["msgBody"]["itemList"]}

    for item in data_to_update["msgBody"]["itemList"]:
        bus_node_id = item["BUS_NODE_ID"]
        direction = item["DIR"]

        if bus_node_id in bus_stop_name_map:
            bus_info = bus_stop_name_map[bus_node_id]
            item["BUSSTOP_NM"] = bus_info["BUSSTOP_NM"]
            item["TOTAL_DIST"] = bus_info["TOTAL_DIST"]

    return data_to_update

# DIR 0 방향의 버스 위치를 확인하고 JSON 형식으로 반환하는 함수
def check_bus_position_dir_0():
    data = added_busPosInfo()

    for item in data["msgBody"]["itemList"]:
        bus_stop_name = item.get("BUSSTOP_NM")
        direction = item["DIR"]

        # DIR이 0일 때 관심 정류장에 해당하는 경우 메시지 출력
        if direction == "0" and bus_stop_name in dir_0_stations_names:
            return json.dumps({"message": "슬슬 타러 나가죠?", "BUSSTOP_NM": bus_stop_name}, ensure_ascii=False, indent=4)

    # 관심 정류장이 아닌 경우
    return json.dumps({"message": "아직 전이거나 지나감", "BUSSTOP_NM": bus_stop_name}, ensure_ascii=False, indent=4)

# DIR 1 방향의 버스 위치를 확인하고 JSON 형식으로 반환하는 함수
def check_bus_position_dir_1():
    data = added_busPosInfo()

    for item in data["msgBody"]["itemList"]:
        bus_stop_name = item.get("BUSSTOP_NM")
        direction = item["DIR"]

        # DIR이 1일 때 관심 정류장에 해당하는 경우 메시지 출력
        if direction == "1" and bus_stop_name in dir_1_stations_names:
            return json.dumps({"message": "슬슬 타러 나가죠?", "BUSSTOP_NM": bus_stop_name}, ensure_ascii=False, indent=4)

    # 관심 정류장이 아닌 경우
    return json.dumps({"message": "아직 전이거나 지나침", "BUSSTOP_NM": bus_stop_name}, ensure_ascii=False, indent=4)

# API 호출 예시
#print(check_bus_position_dir_0())
#print(check_bus_position_dir_1())