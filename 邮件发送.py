import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


sender = "1484193144@qq.com"
to = "1484193144@qq.com"
pwd = "gqjpnynjuorhhaeg"
host = "smtp.qq.com"


msg =MIMEMultipart()
msg["From"] = Header("发件人标题","utf-8")
msg["To"] = Header("收件人标题","utf-8")
msg["Subject"] = Header("测试报告","utf-8")

att = MIMEText(open("HtmlTestRunner生成的报告.html","rb").read(),"base64","utf-8")

att["Content-Type"] = "applation/octet-steam"
att["Content-Disposition"] = "atachtment;filename=报告.html"
msg.attach(att)


smtp = smtplib.SMTP()
smtp.connect(host,25)
smtp.login(sender,pwd)
smtp.sendmail(sender,to,msg.as_string())
smtp.quit()
print("邮件发送成功！！！")