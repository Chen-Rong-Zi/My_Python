
# coding=utf-8
from urllib import request as rq
from urllib import parse as pr
from ua_pool import ua_list as UA
from bs4 import BeautifulSoup as BS
import random

class clawer:
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'



   # 拼接url，更改url属性
    def combine_url(self,content):
        search = pr.quote(content['search'])
        pagenumber = pr.quote(content['pagenumber'])
        self.url = self.url.format(search, pagenumber)


    # 爬取网页，返回html列表
    def get_html(self):
        # 1.封装请求
        head = {'UserAgent':random.choice(UA)}
        request = rq.Request(self.url,headers=head)

        # 2.发送请求，返回应答对象
        response = rq.urlopen(request)
        bs = BS(response.read().decode(), 'html.parser')
        html = bs.prettify()

        print(html)
        return html



def main():
    # 实例化一个爬虫
    spd = clawer()
    # 
    search = str(input('您要搜索的吧：'))
    pagenumber = str(input('您要爬取的页数：'))

    dic = {'search':search,'pagenumber':pagenumber}
    spd.combine_url(dic)
    print(spd.url)
    spd.get_html()

    pass



if __name__ == '__main__':
    main()
