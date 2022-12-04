# coding=UTF-8
from 立方体 import 立方体
from 连线   import 连线  as 连线_original
import matplotlib.pyplot as plt


class 立体几何:
    def __init__(self, distribution=111):
        self.axis = plt.subplot(projection='3d')
        self.axis.set_title('Title')
        self.axis.set_xlabel('X')
        self.axis.set_ylabel('Y')
        self.axis.set_zlabel('Z')

    def 直棱柱(self, lt, wt, ht):pass
        # (<++>)

    def 棱锥(self, mode, lt):pass
        # (<++>)

    def 连线(self, lst, style='-', color='black'):
        # switch the function to the method
        连线_original(self.axis, lst, style, color)

    def highlight(self, S, label='', color='red'):
        # highlight the spot you plotted
        label = str(S) if label == '' else label

        self.axis.text(S[0], S[1], S[2] , label, color=color)

    def highlight_all(self, lst):
        for D in lst:
            self.highlight(D, str(D))
        

    def show(self):
        plt.show()



class Cube(立体几何):

    def __init__(self, wt=2, lt=2, ht=2, reverse=False):
        立体几何.__init__(self)
        if reverse == True:
            A   = (wt,  0,  0)
            B   = (wt, lt,  0)
            C   = (0 , lt,  0)
            D   = (0 ,  0,  0)
            A1  = (wt,  0, ht)
            B1  = (wt, lt, ht)
            C1  = (0 , lt, ht)
            D1  = (0 ,  0, ht)
        if reverse == False:
            A   = (0 ,  0,  0)
            B   = (wt,  0,  0)
            C   = (wt, lt,  0)
            D   = (0 , lt,  0)
            A1  = (0 ,  0, ht)
            B1  = (wt,  0, ht)
            C1  = (wt, lt, ht)
            D1  = (0 , lt, ht)
        self.A  = A
        self.B  = B
        self.C  = C
        self.D  = D
        self.A1 = A1
        self.B1 = B1
        self.C1 = C1
        self.D1 = D1

        self.tip_lst = [A, B, C, D, A1, B1, C1, D1 ]

    def plot(self):
        self.连线( self.tip_lst[ :4])
        self.连线( self.tip_lst[4: ])
        self.连线((self.tip_lst[0], self.tip_lst[4]))
        self.连线((self.tip_lst[1], self.tip_lst[5]))
        self.连线((self.tip_lst[2], self.tip_lst[6]))
        self.连线((self.tip_lst[3], self.tip_lst[7]))

    def highlight_tips(self, A = 'A', B = 'B', C = 'C', D = 'D', A1 = 'A1', B1 = 'B1', C1 = 'C1', D1 = 'D1'):
        self.highlight(self.A, A )
        self.highlight(self.B, B )
        self.highlight(self.C, C )
        self.highlight(self.D, D )
        self.highlight(self.A1, A1)
        self.highlight(self.B1, B1)
        self.highlight(self.C1, C1)
        self.highlight(self.D1, D1)



if __name__ == '__main__':
    # This is an example / test for the requirements
    a    = 立体几何()  # Function  return an object_
    cube = Cube(1, 2, 3)
    cube . plot()
    cube . highlight_tips()
    # color = 'red'
    # 
    # cube = a.直棱柱(wt, lt, ht)
    # cube.show_tip(color)
    # 
    # mode = '正三棱锥'         # mode argument such as 正四棱锥,正三棱锥,直角棱锥
    # lengzhui = a.棱锥(mode, lt=9)
    # lengzhui.show_tip(color)
    




    # data
    exp  = 4 / (3 **(0.5))
    A    = (0, 0, 0)
    B    = (2, 0, 0)
    C    = (1, 3 **(0.5), 0) 
    D    = (0, exp, 0)
    E    = (0.5, 0.5 * 3 ** (0.5), 1)
    O    = (1, 0, 0)
    P    = (0, 0, 2)

    连线 = a.连线
    连线( [A, B, C, D, E]         , color='blue')
    连线( [P, A, P, B, P, C, P, D], color='red' )

    # a.highlight(A,f'{A}', color='red')
    a.show()



