# coding=utf-8
# import ssl
from bs4 import BeautifulSoup
from urllib import request
# ssl._create_default_https_context = ssl._create_unverified_context

head = {'UserAgent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
url  = 'http://www.baidu.com'
rq   = request.Request(url,headers=head)

with request.urlopen(rq) as response:
    content = response.read().decode()
    # print(response.read().decode())
bs   = BeautifulSoup(content,'html.parser')
print(type(bs))
print(bs)
print(bs.prettify())
