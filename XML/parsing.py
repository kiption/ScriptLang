
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import xml.etree.ElementTree as ET              # elment 관리에 사용할 클래스

#인증키
My_API_Key = unquote('479bf253ef6045b9ad99cc507e191013')
#url
xmlUrl = 'https://openapi.gg.go.kr/FreeChargeWiFi'

##### global
list_total_count = 4490
list_current_page = 1
DataDoc = []
wifi_list = []

def connectOpenAPI():
    global list_current_page, DataDoC

    while list_current_page <= 5:
        queryParams = '?' + urlencode(
            {
                quote_plus('Key'): My_API_Key,    # 인증키
                quote_plus('pIndex'): list_current_page,   # 페이지 위치
                quote_plus('pSize'): 1000,  # 페이지 당 요청 숫자
             }
        )
        res = Request(xmlUrl+queryParams)
        res.get_method = lambda: 'GET'
        response_body = urlopen(res).read()             # 응답 객체를 바이트 배열로 읽는다.

        xmlobj = response_body.decode('utf-8')          # 바이트 배열을 문자열 배열로 변환
        try:
            tree = ET.ElementTree(ET.fromstring(xmlobj))
            root = tree.getroot()
        except Exception:
            print("Element Tree parsing Error : maybe the xml document is not corrected.")
            exit()

        for item in root.iter('row'):
            row = {}
            for child in list(item):
                row[child.tag] = child.text
            DataDoc.append(row)

        list_current_page += 1


def SearchWifi(SIGUN):
    global wifi_list
    wifi_list.clear()

    for item in DataDoc:
        if item['SIGUN_NM'] == SIGUN:
            wifi_list.append(item)

connectOpenAPI()
