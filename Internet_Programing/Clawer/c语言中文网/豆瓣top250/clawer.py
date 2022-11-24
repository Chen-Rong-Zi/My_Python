# coding=utf-8
from urllib import request as rq
from urllib import parse as pr
from ua_pool import ua_list as UA
# from bs4 import BeautifulSoup as BS
import random
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



class Clawer:
    url = 'https://movie.douban.com/top250'
    def __init__(self):pass



   # 拼接url，更改url属性
    def combine_url(self, url, string=''):
        content = pr.quote(string)
        url = url + string
        return url



    # 爬取网页，返回html列表
    def get_html(self, url):
    # 老三样，万用方法
        # 1.封装请求
        head = {'UserAgent':random.choice(UA)}
        request = rq.Request(url,headers=head)
        try:
            # 2.发送请求，返回应答对象
            response = rq.urlopen(request, timeout=3)
            # 3.读取(byte)html，bs4使html更符合规范
            # bs = BS(response.read().decode(), 'html.parser')
            html = response.read().decode()
            # print(html[300:500])
            return html
        except Exception as e:
            print('get_html error!!')


    # 保存html文件
    def save_html(self, html, dir_path='./'):
        filename = dir_path + '.html'
        with open(filename, 'w', encoding='utf-8') as f:
            try:
                f.write(html)
            except:
                print('save_html error!')
            print(filename)



    # 方法调用部分，流程控制中心
    def run(self, url, dir_path='./'):
    # 简单的示范，推荐使用时重构run方法
        # 1.url的编码、拼接,返回新url
        '''    url参数无默认值
               string参数默认为空字符串'''
        url = self.combine_url(url)
        
        # 2.发送请求，返回html
        '''    url参数无默认值'''
        html = self.get_html(url)
        
        # 3.保存html文件
        '''    url参数无默认值
               dir_path参数默认为'./'
               html参数无默认值，须为字符串'''
        self.save_html(url, html, dir_path)


# 测试
def main():
    start = time.time()
    
    sp = Clawer()
    url = sp.url
    sp.run(url)
    
    end = time.time()
    print(f'运行时间：{end-start}')
    
    
    
if __name__ == '__main__':
    main()
