# coding=utf-8

# 文本
with open('welcome.txt','r',encoding='utf-8') as t:
    text_lines = t.readlines()
    # print(text_lines)

word_dic = {}    
for line in text_lines:
    # print(text_lines)
    words = line.split()
    # print(words)
    for word in words:
        try:
            word_dic[word] += 1
        except:
            word_dic[word] = 1
vk_list = []            
kv_list = list(word_dic.items())
for k,v in kv_list:
    vk_list.append((v,k))
print(sorted(vk_list,reverse=True)[0:10])



        


