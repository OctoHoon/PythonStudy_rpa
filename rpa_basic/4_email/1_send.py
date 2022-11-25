import smtplib
from account import *

# SMTP(Simple Mail Transfer Protocol)는
# e-mail을 컴퓨터에서 다른 컴퓨터로 전송할 때
# 사용하는 메일 서버의 기본 프로토콜

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # SMPT 서버와 연결이 잘 수립되는지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인

    subject = "test mail" # 메일 제목
    body = "mail body" # 메일 본문

    msg = f"Subject: {subject}\n{body}"

    # 발신자 , 수신자 , 정해진 형식의 메시지
    smtp.sendmail(EMAIL_ADDRESS, "sakonghoon40@gmail.com", msg)

