import sys
import telepot
from urllib.request import urlopen
from urllib.parse import unquote,quote
import traceback
from xml.etree import ElementTree

key = unquote('479bf253ef6045b9ad99cc507e191013')                                       # 무료 와이파이 api key
# TOKEN = '5383087654:AAE7LFzA831IH-hfMcy8nAlWJLiqsNvSGfw'                              # 세철 텔레그램 봇 토큰
TOKEN = '5580851446:AAEbftc3YGjBaY2KjmD0b5PoTX6bbRNagvQ'                                # 기태 텔레그램 봇 토큰

MAX_MSG_LENGTH = 300
baseurl ='https://openapi.gg.go.kr/FreeChargeWiFi'+ '?KEY=' + key
bot = telepot.Bot(TOKEN)

# loc_param: 도시이름
# 반환 : 와이파이 상세정보를 문자열로 표현한 리스트
def getData(loc_param):
    res_list = []

    url = baseurl+'&SIGUN_NM='+quote(loc_param)
    res_body = urlopen(url).read()
    strXml = res_body.decode('utf-8')
    tree = ElementTree.fromstring(strXml)
    items = tree.iter("row") # return list type
    index = 1
    for item in items:
        PlaceAddr = '설치장소(상세) - ' + item.find("INSTL_PLC_DETAIL_DTLS").text      # 설치장소상세
        try:
            LoadAddr = '도로명 주소 - ' + item.find("REFINE_ROADNM_ADDR").text  # 도로명 주소
        except:
            LoadAddr = '도로명 주소 - 없음'

        LoadAddrPlus ='지번 주소 - ' + item.find("REFINE_LOTNO_ADDR").text       # 지번 주소
        SSID = 'SSID - ' + item.find("WIFI_SSID_INFO").text                  # SSID
        NamePlace = '관리기관 - ' + item.find("MANAGE_INST_NM").text             # 관리 기관명
        PhoneNumber = '전화번호 - ' +item.find("MANAGE_INST_TELNO").text       # 전화번호
        row = '[' + str(index) + '] ' + PlaceAddr + '\n' + LoadAddr + '\n' + LoadAddrPlus + '\n' + SSID + '\n' + NamePlace + '\n(' + PhoneNumber + ')\n'
        res_list.append(row)
        index += 1
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except: # 예외 정보와 스택 트레이스 항목을 인쇄.
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)