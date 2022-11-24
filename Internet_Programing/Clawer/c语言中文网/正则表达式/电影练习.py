# coding=utf-8
import re
html = """
<div class="movie-item-info">
<p class="name">
<a title="你好，李焕英">你好，李焕英</a>
</p>
<p class="star">
主演：贾玲,张小斐,沈腾
</p>    
</div>
<div class="movie-item-info">
<p class="name">
<a title="刺杀，小说家">刺杀，小说家</a>
</p>
<p class="star">
主演：雷佳音,杨幂,董子健,于和伟
</p>    
</div> 
"""
# 标题 主演

# pattern = re.compile(r'<div.*?title="(.*?)".*?star">(.*?)</p.*?div>', re.S)
pattern = re.compile(r'<div(.*)>', re.S)
for i in pattern.findall(html):
    print(i)
for info in pattern.findall(html):
    for mt in info:
        print(mt,end='')


