# coding=UTF-8
import matplotlib as mpl
import matplotlib.pyplot as plt



def 成组(tp_lst):
    x_lst = []
    y_lst = []
    z_lst = []
    for spot in tp_lst:
        for i in range(3):
            x_lst.append(spot[0])
            y_lst.append(spot[1])
            z_lst.append(spot[2])

    return x_lst, y_lst, z_lst



# lst是包含数个点(三维坐标)元组的集合, 通过成组()解包 将
# 数个坐标改造成集合构成的xyz_lst, 交给连线()画图
def 连线(axis, lst, style = '-', color='black'):
    x_lst, y_lst, z_lst = 成组(lst)

    for i in range(len(x_lst)):
        I = i + 1 if i + 1 < len(x_lst) else 0

        axis.plot((x_lst[i], x_lst[I]), 
                  (y_lst[i], y_lst[I]), 
                  (z_lst[i], z_lst[I]), style, color=color
        )




def test(first_floor, second_floor):
    axis = plt.subplot(projection = '3d')
    axis.set_xlabel('x')
    axis.set_ylabel('y')
    axis.set_zlabel('z')

    x_first , y_first , z_first  = 成组(first_floor)
    x_second, y_second, z_second = 成组(second_floor)


    exp = 4 / (3 **(0.5)   )
    A = (0, 0, 0)
    B = (2, 0, 0)
    C = (1, 3 **(0.5), 0) 
    D = (0, exp, 0)
    E = (0.5, 0.5 * 3 ** (0.5), 1)
    O = (1, 0, 0)
    P = (0, 0, 2)
    连线(axis, [A, B, C, D])
    连线(axis, [P, A, P, C, P, B, P, D])
    连线(axis, [A, C])
    连线(axis, [A, E, B])


    axis.text(A[0], A[1], A[2], 'A', color = 'red')
    axis.text(B[0], B[1], B[2], 'B', color = 'red')
    axis.text(C[0], C[1], C[2], 'C', color = 'red')
    axis.text(D[0], D[1], D[2], 'D', color = 'red')
    axis.text(E[0], E[1], E[2], 'E', color = 'red')
    axis.text(P[0], P[1], P[2], 'P', color = 'red')
    axis.text(O[0], O[1], O[2], 'O', color = 'green')






if __name__  == "__main__":
    first  = [(0, 0, 0), (0, 2, 0), (2, 2, 0)]
    second = [(0, 0, 2), (0, 2, 2), (2, 2, 2)]
    test(first, second)
    plt.show()
