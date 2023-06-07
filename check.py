#_*_coding:utf-8 *

import subprocess
import os
import time
from dateutil.parser import parse

webSiteName = 'goodfish证书透明'# 网站名
yourBlogUrl = 'blog.goodfish.site'# 博客url
webSiteList = ['wordpress.goodfish.site','blog.goodfish.site', 'ssl.goodfish.site', 'api.goodfish.site', 'file.goodfish.site'] #需要检查的域名列表，无需填写协议名，同时支持端口号。
html_code ="""
<!DOCTYPE html>
<html lang="zh-CN"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link rel="preload" href="https://ssl.goodfish.site/icons/material-icons/MaterialIcons-Regular.woff2" as="font" type="font/woff2" crossorigin="">
<title itemprop="name">""" + webSiteName +"""</title>
<meta name="theme-color" content="#607d8b">
<link rel="stylesheet" type="text/css" href="css/mdui.min.css">
<style>
body{font-family:"Helvetica Neue", Helvetica, Microsoft Yahei, sans-serif; background-color:rgb(237, 237, 237)}.mdui-panel{margin-top:80px;margin-bottom:20px;max-width:800px}.mdui-panel-item-title{width:62%;min-width:62%}.item-title{color:rgba(0,0,0,.54)}.item-wr{color:rgba(255,0,0,.7)}.mdui-progress{width:100%;position:absolute;bottom:0;left:0;border-radius:0;height:7px}.mdui-panel-item-body{position:relative}.mdui-panel-item-summary{padding-right:12px}.body-wr{background-color:rgba(255,0,0,.7);color:white;padding:3px;margin:3px;border-radius:3px}
</style>
<style>
.translatorExtension {
  font-family: Segoe UI, "Segoe UI Web (West European)", -apple-system,
    BlinkMacSystemFont, Roboto, Helvetica Neue, sans-serif;
  display: none;
  padding: 4px;
  position:absolute;
  z-index:999999999;
  max-width: 30vw;
  line-height: 1.5em;
  border: 1px solid #000;
  background: #fff;
  color: #000;
  font-size: 15px;
}
</style></head>
<body class="mdui-theme-primary-blue-grey mdui-loaded">
<div class="mdui-appbar mdui-appbar-fixed">
  <div class="mdui-toolbar mdui-color-theme">
    <span class="mdui-typo-headline">""" + webSiteName +"""</span>
    <div class="mdui-toolbar-spacer"></div>
    <button mdui-menu="{target: '#about'}" class="mdui-btn mdui-btn-icon"><i class="mdui-icon material-icons">more_vert</i></button>
    <ul class="mdui-menu" id="about">
        <li class="mdui-menu-item">
            <a href='""" + yourBlogUrl+"""' target="_blank" class="mdui-ripple">我的博客</a>
        </li>
        </ul>
          </div>
</div>
<div class="mdui-panel mdui-panel-gapless mdui-center" mdui-panel="">
"""
for i in range(len(webSiteList)):
    try:
        comm1 = "curl https://"+webSiteList[i]+" --connect-timeout 10 -v -s -o /dev/null 2>/tmp/ca.info ; cat /tmp/ca.info | grep 'start date: '" #利用curl检查证书开始时间，注意一下ca.info保存路径，connect-timeout可以控制超时时间，避免假死
        out_bytes1 = subprocess.check_output(comm1, shell=True)
        out_text1 = out_bytes1.decode('utf-8')
        comm2 = "cat /tmp/ca.info | grep 'expire date: '" #检查证书到期时间
        out_bytes2 = subprocess.check_output(comm2, shell=True)
        out_text2 = out_bytes2.decode('utf-8')
        comm3 = "cat /tmp/ca.info | grep 'issuer: '" #获取证书颁发机构
        out_bytes3 = subprocess.check_output(comm3, shell=True)
        out_text3 = out_bytes3.decode('utf-8')
        os.system('rm -f /tmp/ca.info')
        print(float(str((parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) - parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))) / (parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) - parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text1[-25:-5],"%b %d %H:%M:%S %Y"))))))*100)
        if int(str(parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) - parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))[0:2]) <= 10:
            time_data_ins = str(parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) - parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))[0:2]
            '''
            import smtplib
            smtp = smtplib.SMTP_SSL("smtp.qq.com")
            smtp.login(user="2143495907@qq.com", password="vlsuftncvgfqebeh")
            from email.mime.text import MIMEText
            from email.header import Header
            message = MIMEText('SSL证书过期提醒', 'plain', 'utf-8')
            message['From'] = Header("sever", 'utf-8')  # 发件人的昵称
            message['To'] = Header("goodfish", 'utf-8')  # 收件人的昵称
            tifd = '您的网站'+webSiteList[i]+'的SSL证书,还有'+time_data_ins+'天就过期了，请及时续签'
            message['Subject'] = Header(tifd, 'utf-8')  # 定义主题内容
            smtp.sendmail(from_addr="2143495907@qq.com", to_addrs="hy110724@163.com", msg=message.as_string())
            print('ye')
            '''
            join_code = """
            <div class="mdui-panel-item">
            <div class="mdui-panel-item-header">
                <div class="mdui-panel-item-title">""" + webSiteList[i] + """</div>
                <div class="mdui-panel-item-summary">
                    <span class="item-wr">即将到期</span>
                </div>
                <i class="mdui-panel-item-arrow mdui-icon material-icons">keyboard_arrow_down</i>
            </div>
            <div class="mdui-panel-item-body">
                <p><span class="item-title">最后检查</span>&nbsp;&nbsp;""" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + """&nbsp;</p>
                    <p><span class="item-title">开始时间</span>&nbsp;&nbsp;""" + str(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text1[-25:-5],"%b %d %H:%M:%S %Y"))) + """</p>
                <p><span class="item-title">到期时间</span>&nbsp;&nbsp;""" + str(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) + """</p>
                <p><span class="item-title">剩余</span>&nbsp;&nbsp;""" + str(parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) - parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))[0:2] + """天</p>
                <p><span class="item-title">颁发机构</span>&nbsp;&nbsp;""" + out_text3[11:-1].replace('"', "'") + """</p>
                <div class="mdui-progress">
                    <div class="mdui-progress-determinate" style="width: """ + str(100-float(str((parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) - parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))) / (parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) - parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text1[-25:-5],"%b %d %H:%M:%S %Y"))))))*100) + """%;"></div>
                </div>
                </div>
            </div>
            """
        else:
            join_code = """
            <div class="mdui-panel-item">
            <div class="mdui-panel-item-header">
                <div class="mdui-panel-item-title">""" + webSiteList[i] + """</div>
                <div class="mdui-panel-item-summary">正常</div>
                <i class="mdui-panel-item-arrow mdui-icon material-icons">keyboard_arrow_down</i>
            </div>
            <div class="mdui-panel-item-body">
                <p><span class="item-title">最后检查</span>&nbsp;&nbsp;""" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + """&nbsp;</p>
                    <p><span class="item-title">开始时间</span>&nbsp;&nbsp;""" + str(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text1[-25:-5],"%b %d %H:%M:%S %Y"))) + """</p>
                <p><span class="item-title">到期时间</span>&nbsp;&nbsp;""" + str(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) + """</p>
                <p><span class="item-title">剩余</span>&nbsp;&nbsp;""" + str(parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) - parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))[0:2] + """天</p>
                <p><span class="item-title">颁发机构</span>&nbsp;&nbsp;""" + out_text3[11:-1].replace('"', "'") + """</p>
                <div class="mdui-progress">
                    <div class="mdui-progress-determinate" style="width: """ + str(100-float(str((parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) - parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))) / (parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text2[-25:-5],"%b %d %H:%M:%S %Y"))) - parse(time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(out_text1[-25:-5],"%b %d %H:%M:%S %Y"))))))*100) + """%;"></div>
                </div>
                </div>
            </div>
            """
    except Exception as e:
        print(e)
        os.system('rm -f /tmp/ca.info')
        join_code = """
        <div class="mdui-panel-item">
        <div class="mdui-panel-item-header">
            <div class="mdui-panel-item-title">""" + webSiteList[i] + """</div>
            <div class="mdui-panel-item-summary">
                <span class="item-wr">连接异常</span>
            </div>
            <i class="mdui-panel-item-arrow mdui-icon material-icons">keyboard_arrow_down</i>
        </div>
        <div class="mdui-panel-item-body">
            <p><span class="item-title">最后检查</span>&nbsp;&nbsp;""" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + """&nbsp;<span class="body-wr">连接超时</span></p>
                <p><span class="item-title">开始时间</span>&nbsp;&nbsp;NaN</p>
            <p><span class="item-title">到期时间</span>&nbsp;&nbsp;NaN</p>
            <p><span class="item-title">剩余</span>&nbsp;&nbsp;0天</p>
            <p><span class="item-title">颁发机构</span>&nbsp;&nbsp;NaN</p>
            <div class="mdui-progress">
                <div class="mdui-progress-determinate" style="width: 100%;"></div>
            </div>
            </div>
        </div>
        """
    html_code += join_code
    time.sleep(1) #睡一会儿，免得太High

html_code += """
        </div>
           <script src="js/mdui.min.js"></script>
           <div id="translatorExtensionContainer" class="translatorExtension" style="display: none;"></div><div class="translatorExtension" style="position: fixed; display: flex; justify-content: center; bottom: -40vh; left: 0px; right: 0px; margin: 0px auto; width: 100%; transition: all 80ms ease 0s; visibility: hidden;"></div></body></html>
"""

print("Check OK")
with open("/www/wwwroot/ssl/index.html", 'w') as file_object:
    file_object.write(html_code)
