import requests
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from xml.dom.minidom import parse               # 파일 파싱에 사용할 함수
import xml.etree.ElementTree as ET              # elment 관리에 사용할 클래스

#인증키
My_API_Key = unquote('479bf253ef6045b9ad99cc507e191013')

#url
xmlUrl = 'https://openapi.gg.go.kr/FreeChargeWiFi'

list_total_count = 4490
list_current_count = 1

queryParams = '?' + urlencode(
    {
        quote_plus('Key') : My_API_Key,    # 인증키
        quote_plus('pIndex') : 1,   # 페이지 위치
        quote_plus('pSize') : 100,  # 페이지 당 요청 숫자
     }
)

DataDoc = []
xmlobj = None

res = Request(xmlUrl+queryParams)
res.get_method = lambda: 'GET'
response_body = urlopen(res).read()

xmlobj = response_body.decode('utf-8')
tree = ET.ElementTree(ET.fromstring(xmlobj))
root = tree.getroot()

DataDoc = []

for item in root.iter('row'):
    row = {}
    for child in list(item):
        row[child.tag] = child.text
    DataDoc.append(row)

for item in DataDoc:
    print(item['SIGUN_NM'],item['REFINE_WGS84_LAT'])

