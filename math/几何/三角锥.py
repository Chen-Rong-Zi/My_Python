import matplotlib.pyplot as plt

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
