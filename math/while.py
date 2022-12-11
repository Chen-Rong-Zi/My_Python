# coding=UTF-8
a = 1
while a < 65535 :     # 遍历1-100
    a  += 1

    b   = 1
    while b < a - 1:
        b   += 1

        if a % b == 0:  # 余数为零则不继续循环
            break

    else:print(a)       # 如果break则不打印

