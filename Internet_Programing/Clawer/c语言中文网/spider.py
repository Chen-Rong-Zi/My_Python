# coding=utf-8
import urllib.request as rq
import urllib.parse as pr
from ua_pool import ua_list as UA 

end = '  结束\n\n'
url = 'https://www.baidu.com/s?'

# 请求对象
    # 伪装
head = {"User-Agent": UA[0]}
print(head)

a = {'wd':'爬虫'}
b = 'wd=爬虫'
    # url编码
u = url +  '/s?'+pr.urlencode(a)
# u = url + pr.quote(b)
    # url解码
# i = pr.unquote('https://www.baidu.com/s?/s?wd=%E7%88%AC%E8%99%AB')
# print(u+'\n'+i)

request = rq.Request(url=url,headers=head)
# print(response.read().decode('gbk'))
# print(response.getcode(),end=end)

# 响应对象
response = rq.urlopen(request)
# print(response)

# html文本
html = response.read().decode('utf-8')
# print('\n'+html)

