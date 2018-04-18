#coding=utf-8
import re
import requests

url = 'http://www.baidu.com'
data={"username":"admin","password":123456}
r = requests.get(url,data)
r.encoding = "utf-8"
print(r.text)

p1 = r"关于百度"
pattern1 = re.compile(p1)
print (pattern1.findall(r.text))