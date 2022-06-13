import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import parsing

def makeHtml(data):
    from xml.dom.minidom import getDOMImplementation
    for wifi in parsing.wifi_list:
        if wifi['TMP01'] == data:
            impl = getDOMImplementation()

            newdoc = impl.createDocument(None, "html", None)
            top_element = newdoc.documentElement
            header = newdoc.createElement('header')
            top_element.appendChild(header)

            body = newdoc.createElement('body')

            b = newdoc.createElement('b')
            sigunText = newdoc.createTextNode("지역:" + wifi['TMP01'])
            b.appendChild(sigunText)
            body.appendChild(b)

            p = newdoc.createElement('p')
            lotaddrText = newdoc.createTextNode("지번 주소:" + wifi['REFINE_LOTNO_ADDR'])
            p.appendChild(lotaddrText)
            body.appendChild(p)

            p = newdoc.createElement('p')
            roadaddrText = newdoc.createTextNode("도로명 주소:" + wifi['REFINE_ROADNM_ADDR'])
            p.appendChild(roadaddrText)
            body.appendChild(p)

            p = newdoc.createElement('p')
            LOGTText = newdoc.createTextNode("위도:" + wifi['REFINE_WGS84_LOGT'])
            p.appendChild(LOGTText)
            body.appendChild(p)

            p = newdoc.createElement('p')
            LATText = newdoc.createTextNode("경도:" + wifi['REFINE_WGS84_LAT'])
            p.appendChild(LATText)
            body.appendChild(p)

            i = newdoc.createElement('i')
            TELNOText = newdoc.createTextNode("전화번호:" + wifi['MANAGE_INST_TELNO'])
            i.appendChild(TELNOText)
            body.appendChild(i)

            top_element.appendChild(body)

            return newdoc.toprettyxml()

# for i in str:
#     print(i)
# str = s['TMP01'] + "의 와이파이 상세 정보" + '\n' + \
#                       "지번주소:" + s['REFINE_LOTNO_ADDR'] + '\n' + \
#                       '도로명주소:' + s['REFINE_ROADNM_ADDR'] + '\n' + \
#                       '위도:' + s['REFINE_WGS84_LOGT'] + '\n' + \
#                       '경도:' + s['REFINE_WGS84_LAT'] + '\n' + \
#                       '전화번호:' + s['MANAGE_INST_TELNO'] + '\n'


def sendMail(email_to, content):
    msg = ""
    senderAddr = "rlxo8749@gmail.com"
    recipientAddr = email_to

    msg = MIMEMultipart('alternative')

    msg['Subject'] = "ScriptLanguage_WhereFi"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    file = open('wifi_details.html','w',encoding='UTF-8')
    file.write(makeHtml(content))
    file.close()

    htmlFD = open("wifi_details.html",'rb')
    htmlPart = MIMEText(htmlFD.read(),'html',_charset='UTF-8')
    htmlFD.close()

    msg.attach(htmlPart)

    s = smtplib.SMTP("smtp.gmail.com",587)  # SMTP 서버와 연결
    s.starttls()    # SMTP 연결을 TLS (Transport Layer Security) 모드로전환

    s.login('rlxo8749@gmail.com', 'tujyuxcomqipqsus')
    s.sendmail('rlxo8749@gmail.com', [email_to], msg.as_string())
    s.close()