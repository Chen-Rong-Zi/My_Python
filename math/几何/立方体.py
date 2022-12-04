# coding=utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import types
from 连线 import 连线




def 立方体(distribution=111 , lt=4, wt=4, ht=4, title = 'CUBE', border = 0 ):
    # 立方体绘图
    x    = [0,   0, lt, lt,  0,  0, lt,  0, lt]
    y    = [0,  wt, wt,  0,  0,  0,  0, wt, wt]
    z    = [0,   0,  0,  0,  0, ht, ht, ht, ht]
    add  = [ht, ht, ht, ht, ht, ht, ht, ht, ht]

    axis = plt.subplot(distribution, projection='3d')

    # axis.plot(x[:5], y[:5],   z[:5], 'b-')                            # 底面
    # axis.plot(x[:5], y[:5], add[:5], 'b-')                            # 顶面
    # for i in range(4):
    #     axis.plot((x[i], x[i]), (y[i], y[i]), (z[i], add[i]), 'b-') # 侧棱

    # x, y, z轴
#     axis.set_xlim(-border, lt + border)
#     axis.set_ylim(-border, wt + border)
#     axis.set_zlim(-border, ht + border)
    axis.set_xlabel('X')
    axis.set_ylabel('Y')
    axis.set_zlabel('Z')

  # 动态添加属性, 方法
    axis.x = x
    axis.y = y
    axis.z = z

    def show_tips(self):
        lst  = ['A', 'B', 'C', 'D', 'A1', 'B1', 'C1', 'D1']
        for j in range(len(lst)):
            self.text(self.x[j], self.y[j], self.z[j], lst[j], color = 'red')

        axis.show_tips = types.MethodType(show_tips, axis)


    A  = ( 0,  0,  0)
    B  = (wt,  0,  0)
    C  = (wt, lt,  0)
    D  = ( 0, lt,  0)
    A1 = ( 0,  0, ht)
    B1 = (wt,  0, ht)
    C1 = (wt, lt, ht)
    D1 = ( 0, lt, ht)
    连线(axis, [A , B , C , D , A ])
    连线(axis, [A1, B1, C1, D1, A1])
    连线(axis, [A , A1])
    连线(axis, [B , B1])
    连线(axis, [C , C1])
    连线(axis, [D , D1])






if __name__ == '__main__':
    cube = 立方体(111, 2, 1000, 8)
    plt.show()
