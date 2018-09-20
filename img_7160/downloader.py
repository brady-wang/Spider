# *_*coding:utf-8 *_*
import string
from urllib.parse import quote

import requests
class Downloader(object):
    def Download(self,url):
        headers = {"User-Agent": "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
        url_ = quote(url, safe=string.printable)
        response = requests.get(url_,headers=headers)
        if response.status_code == 200:
<<<<<<< HEAD
            response.encoding='gb2312'
=======
            response.encoding='utf-8'
            #fout = open('output.html', 'w', encoding='utf-8')
            #fout.write(response.text)
>>>>>>> 069d225b498d4ce3c199324fad03bb6a2ee1d884
            return response.text
        else :
            return None