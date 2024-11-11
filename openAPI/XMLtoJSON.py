import xml.etree.ElementTree as ET
import json


def convert(xml_data):
    # XML 파싱
    root = ET.fromstring(xml_data)

    # XML 데이터를 딕셔너리로 변환하는 함수
    def xml_to_dict(element):
        data = {}
        for child in element:
            # 하위 요소가 있을 경우 재귀 호출로 하위 딕셔너리 생성
            child_data = xml_to_dict(child) if len(child) else child.text

            # 동일한 태그가 여러 개 있으면 리스트로 처리
            if child.tag in data:
                # 이미 리스트가 존재하는 경우 추가
                if isinstance(data[child.tag], list):
                    data[child.tag].append(child_data)
                else:
                    # 리스트가 없으면 새로 생성
                    data[child.tag] = [data[child.tag], child_data]
            else:
                # 리스트가 필요 없으면 그대로 추가
                data[child.tag] = child_data
        return data

    # 루트 요소를 딕셔너리로 변환 후 JSON으로 변환
    result_dict = xml_to_dict(root)
    result_json = json.dumps(result_dict, ensure_ascii=False, indent=4)

    return result_json

