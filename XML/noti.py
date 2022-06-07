import sys
import telepot
from pprint import pprint
from urllib.request import urlopen
from urllib.parse import unquote
import traceback
from xml.etree import ElementTree
from xml.dom.minidom import parseString

key = unquote('479bf253ef6045b9ad99cc507e191013')
TOKEN = '5383087654:AAE7LFzA831IH-hfMcy8nAlWJLiqsNvSGfw'
MAX_MSG_LENGTH = 300
baseurl ='https://openapi.gg.go.kr/FreeChargeWiFi'+key
bot = telepot.Bot(TOKEN)

def getData(loc_param, date_param):
    res_list = []

    #공공데이터 포털에서 지역 + 기간에
    #해당하는 거래 정보를 가져와서 -> html 해석 -> ‘item’항목들의
    url = baseurl+'&LAWD_CD='+loc_param+'&DEAL_YMD='+date_param
    res_body = urlopen(url).read()
    strXml = res_body.decode('utf-8')
    tree = ElementTree.fromstring(strXml)
    items = tree.iter("item") # return list type

    for item in items:
        PlaceAddr = item.find("설치장소상세").text.strip()
        LoadAddr = item.find("도로명 주소").text
        LoadAddrPlus = item.find("지번 주소").text
        SSID = item.find("SSID").text
        NamePlace = item.find("관리 기관명").text
        PhoneNumber = item.find("전화번호").text
        row = PlaceAddr + '/' + LoadAddr + '/' + LoadAddrPlus + '/' + SSID + '/' + NamePlace + '('+ PhoneNumber+') '
        res_list.append(row)
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except: # 예외 정보와 스택 트레이스 항목을 인쇄.
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)