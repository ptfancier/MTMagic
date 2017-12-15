#encoding:utf-8
import requests
from lxml import html
from PIL import Image, ImageDraw, ImageFont

USERNAME = "改为你的用户名"
PASSWORD = "改为你的密码"
#二次验证应该不支持
LOGIN_URL = "https://tp.m-team.cc/takelogin.php"
URL = "https://tp.m-team.cc/mybonus.php"
session_requests = requests.session()
payload = {
    "username": USERNAME,
    "password": PASSWORD,
}
result = session_requests.post(LOGIN_URL, params = payload, headers = dict(referer = LOGIN_URL))
print(result.headers)
result = session_requests.get(URL, headers = dict(referer = URL))
#tree = html.fromstring(result.content.decode('utf-8'))

str = result.content.decode('utf-8')
print str
pos = str.find(u'目前每小時合計可獲得')
print pos
magic = str[pos+10:pos+25]
pos = magic.find(u'魔力值')
print pos
magic = magic[0:pos]
pos = str.find(u'用你的魔力值（當前')
amount= str[pos+9:pos+40]
pos = amount.find(u'）換東東')
amount= amount[0:pos]
print magic
print amount
data= u'魔力值获取:'+magic+'/h\n'+u'当前魔力值:'+amount;
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('C:/windows/fonts/msyh.ttf', 20)
fillcolor = "#000000"
draw.text((0, 0), data, font=font, fill=fillcolor)
image.save('C:/Apache24/htdocs/magic.jpg', 'jpeg')
