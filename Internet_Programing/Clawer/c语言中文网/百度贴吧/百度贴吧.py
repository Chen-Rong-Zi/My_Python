# coding=utf-8
from urllib import request as rq
from urllib import parse as pr
from ua_pool import ua_list as UA
from bs4 import BeautifulSoup as BS
import random
import time

class clawer:
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
        # print(len(self.url))
    
   # 拼接url，更改url属性
    def combine_url(self,content):
        search = pr.quote(content['search'])
        # print(content['pagenumber'])
        pagenumber = content['pagenumber']
        
        url = self.url.format(search, pagenumber)
        return url
        # print(self.url)
    '''def change(self):
        self.url = {}
        print(self.url)'''
    # 爬取网页，返回html列表    
    def get_html(self, url):
        # 1.封装请求
        head = {'UserAgent':random.choice(UA)}
        request = rq.Request(url,headers=head)
        # 2.发送请求，返回应答对象
        response = rq.urlopen(request)
        bs = BS(response.read().decode(), 'html.parser')
        html = bs.prettify()
        # print(html[300:500])
        return html
    
    def save_html(self, url, html):
        filename = './page/' + url[-4:] + '.html'
        with open(filename, 'w', encoding='utf-8') as f:
            # print('hello')
            f.write(html)
        
    def run(self):
        # input获取url参数
        hub = str(input('您要爬取的吧名：'))
        pagenumber = str(input('您要爬取的页数：'))
        # 多页爬取
        for page in range(int(pagenumber)):
            page = page * 50       
            # print(page)
            # 参数字典
            dic = {'search':hub, 'pagenumber':page}

            url = self.combine_url(dic)
            print(url)
            # 获取html，并保存
            html = self.get_html(url)
            self.save_html(url,html)
            time.sleep(random.random())
    
def main():
    start = time.time()
    
    sp = clawer()
    sp.run()
    # sp.change()
    
    end = time.time()
    print(f'运行时间：{end-start}')
    
if __name__ == '__main__':
    main()
