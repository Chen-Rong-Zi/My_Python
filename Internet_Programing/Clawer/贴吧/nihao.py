# coding=utf-8
from ua_list import ls
import ssl
import bs4 
from urllib import request
ssl._create_default_https_context = ssl._create_unverified_context

head = {'UserAgent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
url = 'https://www.bing.com' 
q = request.Request(url, headers=head)

with request.urlopen(rq) as response:
    content = response.read().decode()

bs = bs4.BeautifulSoup(content,'html.parser')
print(bs.prettify())
with open('bing.html','w',encoding='utf-8') as f:
    f.write(bs.prettify())


