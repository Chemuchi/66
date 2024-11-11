import xml.etree.ElementTree as ET

'''
convert - XML 을 JSON 으로 변환
filtering - convert 를 이용하여 원하는 단어만 필터링해 반환

url = <url>
response = requests.get(url)

convert 사용예시 - 
    convert(response.content)
    
출력시 - 
    print(json.dumps(convert(response.content), indent=4, ensure_ascii=False))

filtering 사용예시 -
    filter_word = ["A", "B", "C"]
    filtering(response.content, filter_word)

출력시 - 
    print(json.dumps(filtering(response.content, filter_word), indent=4, ensure_ascii=False))

'''

# XML 데이터를 JSON으로 변환하는 함수
def convert(xml_data):
    root = ET.fromstring(xml_data)

    def xml_to_dict(element):
        data = {}
        for child in element:
            child_data = xml_to_dict(child) if len(child) else None  # 빈 요소는 None으로 처리
            if child.tag in data:
                if isinstance(data[child.tag], list):
                    data[child.tag].append(child_data)
                else:
                    data[child.tag] = [data[child.tag], child_data]
            else:
                data[child.tag] = child_data
        return data

    result_dict = xml_to_dict(root)

    # msgBody가 비어 있으면 운행 중인 버스가 없음을 메시지로 반환
    if "msgBody" in result_dict and not result_dict["msgBody"]:
        return {"message": "운행중인 버스가 없습니다."}

    return result_dict

# 특정 키만 남기는 필터링 함수
def filtering(xml_data, filter_word):
    json_data = convert(xml_data)

    def filter_dict(data):
        if isinstance(data, dict):
            return {key: filter_dict(value) for key, value in data.items() if key in filter_word or isinstance(value, (dict, list))}
        elif isinstance(data, list):
            return [filter_dict(item) for item in data if isinstance(item, dict)]
        else:
            return data

    filtered_data = filter_dict(json_data)
    return filtered_data

