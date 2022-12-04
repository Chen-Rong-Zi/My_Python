# coding=utf-8
import time

with open('./welcome.txt','r',encoding='utf-8') as f:
    lines = f.read()
    print(lines)
    # print(lines)

for w in lines:
    # fd.write(w)
    print(w,end='')
    time.sleep(0.3)


