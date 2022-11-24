# coding=utf-8
import time
with open('bing.html','r',encoding='utf-8') as f:
    content = f.read()
for word in content:
    print(word,end='')
    time.sleep(0.1)
