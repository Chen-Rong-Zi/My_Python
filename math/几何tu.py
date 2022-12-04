# coding=utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt



def 立方体(distribution=111 , lt=4, wt=4, ht=4, title = 'CUBE', border = 0 ):

    x    = [0,   0, lt, lt,  0,  0, lt,  0, lt]
    y    = [0,  wt, wt,  0,  0,  0,  0, wt, wt]
    z    = [0,   0,  0,  0,  0, ht, ht, ht, ht]
    add  = [ht, ht, ht, ht, ht, ht, ht, ht, ht]

    axis = plt.subplot(distribution, projection='3d')

    axis.plot(x[:5], y[:5],   z[:5], 'b-')                            # 底面
    axis.plot(x[:5], y[:5], add[:5], 'b-')                          # 顶面
    for i in range(4):
        axis.plot((x[i], x[i]), (y[i], y[i]), (z[i], add[i]), 'b-') # 侧棱

    axis.set_xlim(-border, lt + border)
    axis.set_ylim(-border, wt + border)
    axis.set_zlim(-border, ht + border)
    axis.set_xlabel('X')
    axis.set_ylabel('Y')
    axis.set_zlabel('Z')

    return axis



# 三棱锥
def tip( lt, wt, mode='正三棱锥'):
    if mode == '正三棱锥':
        return lt / 2, wt / 2
    elif mode == '直角棱锥':
        return 0 , 0
    else:
        raise ValueError('没有这种模式')


def 三角锥(distribution=111, lt=1, wt=1, ht=1, mode='正三棱锥'):
    global tip
    tip = tip(lt, wt, mode)

    x = [0, lt, lt,  0, 0, tip[0]]
    y = [0,  0, wt, wt, 0, tip[1]]
    z = [0,  0,  0,  0, 0, ht]

    ax = plt.subplot(distribution, projection='3d')

    for i in range(len(x)):
        for j in range(len(x)):
            ax.plot((x[i], x[j]), (y[i], y[j]), (z[i], z[j]), color = 'purple')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    return ax

if __name__ == '__main__':
    三角锥(111, 1, 1, 1)
    plt.show()






if __name__ == '__main__':
    cube = 立方体(222)
    plt.show()
