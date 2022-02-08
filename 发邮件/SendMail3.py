#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

my_sender = '10219556@qq.com'  # 发件人邮箱账号
my_pass = '**********'  # 发件人邮箱密码
my_user = '56619556@qq.com'  # 收件人邮箱账号，我这边发送给自己
my_user2 = 'paigames@163.com'


def mail():
    ret = True
    try:
        # msg = MIMEText('这是测试邮件~', 'plain', 'utf-8')
        # msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        # msg['Subject'] = "kylin发送邮件测试"  # 邮件的主题，也可以说是标题

        ############################
        msgRoot = MIMEMultipart('related')
        # msgRoot['From'] = Header("菜鸟教程", 'utf-8')
        # msgRoot['To'] = Header("测试", 'utf-8')
        # subject = 'Python SMTP 邮件测试'
        # msgRoot['Subject'] = Header(subject, 'utf-8')
        msgRoot['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msgRoot['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msgRoot['Subject'] = "kylin发送邮件测试"  # 邮件的主题，也可以说是标题

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        mail_msg = """
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.isainttech.com">isainttech论坛</a></p>
        <p>图片演示：</p>
        <p><img src="cid:image1"></p>
        """
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        # 指定图片为当前目录
        fp = open('./images/worldmap3.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, my_user2], msgRoot.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
        print(e)
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
