# coding = utf-8
with open('./语法练习/Untitled.py','r',encoding='utf-8') as f:
    content = f.read()
    print(content)
    with open('try.py','w+',encoding='utf-8') as f2:
        f2.write(content)
