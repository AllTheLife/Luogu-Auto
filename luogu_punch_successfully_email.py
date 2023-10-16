import sys
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def email(cookie):
    host_server = 'smtp.163.com'
    sender_163 = 'redefinition2607@163.com'
    pwd = cookie
    receiver = ['redefinition0726@163.com']
    mail_title = '洛谷自动打卡成功'
    mail_content = "洛谷自动打卡成功！\nby GitHub Action"
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_163
    msg['To'] = ";".join(receiver)
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
    smtp = SMTP_SSL(host_server)
    smtp.login(sender_163, pwd)
    smtp.sendmail(sender_163, receiver, msg.as_string())
    smtp.quit()


if __name__ == "__main__":
    email(sys.argv[1])
