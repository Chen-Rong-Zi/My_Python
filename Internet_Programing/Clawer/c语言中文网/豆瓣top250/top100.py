# coding=utf-8
# ~/python/InternetProgramming/clawer/C语言中文网/top100.py
from clawer import Clawer
import re
import time
import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



def save_content(filename, string_lst):
    with open(filename, 'w', encoding='UTF-8') as f:
        try:
            for sr in string_lst:
                content = '  ' + sr + '\n'
                f.write(content)
        except:print('save_content error\n')



def my_re(html, chpt_html='', mode='get_url'):
    url = 'https://www.bqg99.com'
    # re expression get the url
    if mode == 'url':
        rule = '<dd><a href ="(/book/\d+?/\d+?.html)">(.*?)</a></dd>'
        lst = re.findall(rule, html)
        UrlName_dic = {}

        # create the {name:url} dictionary
        for t in lst:
            try:
                u = t[0]        # url
                n = t[1]        # name
                u = url + u
                UrlName_dic[u] = n
            except Exception as e:
                print('my_re get the url Error\n')
                
        return UrlName_dic

    # get the chpt content
    elif mode == 'content':
        try:
            rule_content = r'<br />\s+(.*?)<br />'
            sentence_lst = re.findall(rule_content, chpt_html, re.S)
            return sentence_lst
        except Exception as e:print('my_re get the content Error\n')



class My_Clawer(Clawer):

    def run(self, url):
        html = self.get_html(url)
        # print('successfully get the intro html')

        # get the intro html_url:name
        NameUrl_dic = my_re(html, mode='url')

        # get the chpt_html
        for chpt_nu in range(100, 2310):
            chpt_url = 'https://www.bqg99.com/book/17418/{}.html'.format(chpt_nu)
            chpt_html = self.get_html(chpt_url)

            # save the chpt_html
            chpt_name = './chapter_html/' + NameUrl_dic[chpt_url]
            self.save_html(chpt_html, chpt_name)

            # re expression get the content
            chpt_filename = NameUrl_dic[chpt_url] + '.txt'
            chpt_content = my_re(html, chpt_html, 'content')
            chpt_filename = './chapter/' + chpt_filename
            save_content(chpt_filename, chpt_content)
            print('successfully save one chpt!')

            # stop and rest
            time.sleep(random.randint(1,2))

        # print(chpt_content)


        # except Exception as e:




def main():
    url = 'https://www.bqg99.com/book/17418'
    sp = My_Clawer()
    sp.run(url)




if __name__ == '__main__':
    main()
