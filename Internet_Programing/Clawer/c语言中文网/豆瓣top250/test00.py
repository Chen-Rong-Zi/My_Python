import re

with open('./intro/418.html', encoding='UTF-8') as f:
    html = f.read()


rule        = r'<dd><a href ="(/book/\d+?/\d+?.html)">(.*?)</a></dd>'
lst         = re.findall(rule, html)
UrlName_dic = {}

# create the {name:url} dictionary
for t in lst:
    u              = t[0]        # url
    n              = t[1]        # name
    u              = u
    UrlName_dic[u] = n
print(UrlName_dic['/book/17418/103.html'])
