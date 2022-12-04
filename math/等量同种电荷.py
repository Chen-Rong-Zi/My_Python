#coding=utf-8
import sympy as sy      # 求导模块
import numpy as np      # numpy, 用于形成定义域(数组)
from matplotlib import pyplot as plt



l   = 10
l   = (l/2) ** 2

x   = np.arange(0, 100, 0.1)
add = l + x ** 2
y   = add ** (-1.5)
# y = 1 / y
y   = y * x

plt.plot(x, y)



def x轴():
    # x轴
    y = [0]
    plt.hlines(y, xmin=[0], xmax=[100])
    return



def 求导(原函数):
    # 一阶导函数
    x  = sy.symbols('x')
    y  = x * (l + x ** 2) ** (-1.5)
    df = sy.diff(y, x)

    x_value  = []
    f_value  = []
    df_value = []

    # 带入表达式取值,生成函数上点的的坐标
    for i in np .arange(0, 100, 0.1):
        x_value .append(i)
        f_value .append(y.subs('x', i))
        df_value.append(df.subs('x', i))

    plt.xlabel('x')
    plt.ylabel('E')

    return plt.plot(x_value, df_value)



def main():
    求导(y)
    x轴 ( )
    plt.show()



if __name__ == '__main__':
    main()
