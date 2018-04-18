#encoding=utf-8
import urllib.request

proxy_handler = urllib.request.ProxyHandler(
    {
       'http':'http://115.223.225.110:9000' ,
    }
)
url = "http://www.baidu.com"
opener = urllib.request.build_opener(proxy_handler)
response = opener.open(url)
print(response.read())