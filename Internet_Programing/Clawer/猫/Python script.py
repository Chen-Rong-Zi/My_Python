# coding=utf-8

# 导入必要模块
import urllib
import urllib.request
from bs4 import BeautifulSoup
import re
 


# 获取html
def get_html(request):
    html = urllib.request.urlopen(request)
    html = html.read().decode()
    return html




def get_images(html):
    html_bs  = BeautifulSoup(html,'html.parser')
    # 提取img
    bs_img   = html_bs.find_all('img')
    # 创建空列表
    url_list = []
    
    #添加URL进image_list
    for url in bs_img:
        attrs_dic = url.attrs
        try:
            url_list.append(attrs_dic['data-original'])
        except:pass
    # for url in url_list:
        # print(url)
    # 提取下一页的url
    bs_a          = html_bs.find_all('div',class_="nav-links")
    bs_a_a        = bs_a[0].find_all('a',href=True)
    NextPage_attr = bs_a_a[-1]
    print(NextPage_attr)
    NextPage_link = NextPage_attr.attrs['href']
    NextPage_link = '''http://www.k2r2.com'''+NextPage_link
    print(NextPage_link)
    return url_list, NextPage_link




def save_images(url_list,page=1):
    # 图片序列
    url_sequence = 0

    # 遍历列表，发送post
    for url in url_list: 
        head    = {"User-Agent": "Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    # 封装请求，头部信息
        request = urllib.request.Request(url,headers=head)

        # 发送post,获取图片byte
        image   = urllib.request.urlopen(request)
        print(image.read())
        # 保存图片
        url_sequence = url_sequence + 1
        f_name  = '''./猫咪图片/第{0}页、第{1}张图片.jpg'''.format(page,url_sequence)
        with open(f_name,'ab+') as f_name:
            f_name.write(image.read())




# 递归结构
def continue_get(NextPage_link,times=9):
    url     = NextPage_link
    #包装头部信息
    request = urllib.request.Request(url,headers=head)
    # 获取html
    html    = get_html(request)
    # 获取图片
    url_list, Nextpage_link = get_images(html) 
    # 保存图片
    save_images(url_list,(8-times))
        
    # 递归
    # print('这是第{}次'.format(times))
    if times==1:
        return
    continue_get(Nextpage_link, times-1)




def main():
    url     = 'http://www.k2r2.com/maomai_c36803/'
    global head
    head    = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    # 封装请求，头部信息
    request = urllib.request.Request(url,headers=head)
    # 1.发送post请求，获取html文件
    html    = get_html(request)
    # 2.提取图片链接，返回图片链接列表、下一页的链接
    url_list, NextPage_link = get_images(html)
    # 3.遍历链接列表，重复发送post，获取图片并保存
    save_images(url_list)
    # 4.向第二页发送post请求，继续爬取
    continue_get(NextPage_link, 7)



if __name__ == '__main__':
    main()

'''爬虫程序完结撒花，从2022/9/24 8点至2022/9/25 14点，间断地完成了该程序。复习了BeautifuSoup的使用和文件的打开写入操作。期间学习了递归函数，利用其循环的特点，解决了爬虫爬取下一页面的递归过程。期间在写入文件名时，为了表示第一页、第二页......遇到困难，百思不得其解。原因是我尝试用函数被循环的次数（即是类似for循环中的i的性质）表示页码，但因为利用递归来做到连续多次爬取，无法将for循环融合进去。最终是利用递归函数条件变量（times）和页码间的关系完成，思考良久，终有所得。'''


