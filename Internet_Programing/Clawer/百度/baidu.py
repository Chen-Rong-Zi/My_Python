# coding=utf-8
import urllib
from bs4 import BeautifulSoup



head    = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

url     = 'https://www.baidu.com'
request = urllib.request.Request(url,headers=head)
html    = urllib.request.urlopen(request)
# html = html.read().deocde()

bs      = BeautifulSoup(html,'html.parser')
print(bs.prettify())



# 保存html
with open('./pythonista.html','w+',encoding='utf-8') as f:
    f.write(bs.prettify())
print()





