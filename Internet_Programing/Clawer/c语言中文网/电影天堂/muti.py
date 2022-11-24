from clawer import Clawer
from urllib import request as r
from urllib import parse as q
from ua_pool import ua_list as UA
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



with open('./example.html', 'r', encoding='utf-8') as f:
    html = f.read()
    # html =' <a href="/html/gndy/dyzz/20221117/63165.html" class="ulink">2022年悬疑惊悚《神迹/禁食疑案》BD中英双字</a> '
    rule = '<a href="(/html/.*?/\d*\.html)" class="ulink">(.*?)</a>'
    lst = re.findall(rule, html)
    # print(lst)



#if __name__ == '__main__':
#    url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
#
#    sp = Clawer()
#    html = sp.get_html(url, 'gbk')
#    sp.save_html(html, './example')
