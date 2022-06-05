import smtplib
from email.message import EmailMessage

def sendMail(email_to, content):
    msg = ""
    senderAddr = "rlxo8749@gmail.com"
    recipientAddr = email_to

    # HTML 전달을 위해 컨테이너 역할을 할 수 있는 "multipart/alternative" 타입 사용
    msg = EmailMessage()
    msg.set_content(content)

    msg['Subject'] = "ScriptLanguage_WhereFi"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr


    s = smtplib.SMTP("smtp.gmail.com",587)  # SMTP 서버와 연결
    s.starttls()    # SMTP 연결을 TLS (Transport Layer Security) 모드로전환

    s.login('rlxo8749@gmail.com', 'tujyuxcomqipqsus')
    s.sendmail('rlxo8749@gmail.com', [email_to], msg.as_string())
    s.close()