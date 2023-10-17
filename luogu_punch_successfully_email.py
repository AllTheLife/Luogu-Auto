import sys
import pytz
import datetime
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def email(key, my_email, to_email):
    host_server = 'smtp.163.com'
    sender_163 = my_email
    pwd = key
    receiver = [to_email]
    mail_title = '洛谷自动打卡成功'
    mail_head = """<div style = "text-align: center;">
    <h2>洛谷自动打卡成功</h2>
    <h4>By <a href = "https://github.com/CodingOIer/Luogu-Auto/">Luogu-Auto</a> on GitHub Action at """

    mail_tail = """</h4>
</div>
"""
    mail_content = mail_head + \
        str(datetime.datetime.now(pytz.timezone('Asia/Shanghai'))) + mail_tail
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_163
    msg['To'] = ";".join(receiver)
    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
    smtp = SMTP_SSL(host_server)
    smtp.login(sender_163, pwd)
    smtp.sendmail(sender_163, receiver, msg.as_string())
    smtp.quit()


if __name__ == "__main__":
    email(sys.argv[1], sys.argv[2], sys.argv[3])
