import http.client
import urllib.request
from xml.dom.minidom import parseString

server = "openapi.gg.go.kr/FreeChargeWiFi"
client_id = "c7HPM052dSRrbl7CFtPw"
client_secret = "0fed6dc4e3b4437a8e7b20daecee118d"
conn = http.client.HTTPSConnection(server) 
encText = urllib.parse.quote("사랑")
conn.request( #서버에 GET 요청
    "GET",
    "/v1/search/book.xml?dispaly=10&start=1&query="+encText,
    None,
    {"X-Naver-Client-Id": client_id,
     "X-Naver-Client-Secret": client_secret})
res = conn.getresponse() #openAPI 서버의 답을 받아옴.
if int(res.status) == 200: #cLen = res.getheader("Content-Length") #가져온 데이터 길이
    print(parseString(res.read().decode('utf-8')).toprettyxml())
else:
    print("HTTP request failed: ",res.reason)