# coding=utf-8

'''打印九九乘法表'''

# 遍历每一行
for hang in range(1,10):
    # 遍历这行的每一列
    for lie in range(1,hang+1):
        '''可读性杀手！！！ 除第二列以外其他列间隔为一个空，如果是3或4行则间隔为2个
        空，否则为一个空'''
        end = ' ' if lie != 2 else '  ' if hang == 3 or hang == 4 else ' '


        # 打印乘法算式
        a = '{0}x{1}={2}'.format(hang,lie,hang*lie)
        print(a,end=end)
    # 打印空行  
    print()
