# coding=UTF-8
from 立体几何 import 立体几何



pen = 立体几何()
A = (1 , -2 **(0.5), 0)
B = (2, 0, 0)
D = (0, 0, 0)
C = (0, 2, 0)
B = (2, 0, 0)
P = (1, 0, 2 **(0.5))
F = (1, 0, 0)
pen.连线([B, D , C] )
pen.连线([B, D , A] )
pen.连线([P, D , B] )
pen.连线([P, D , C] )
pen.连线([P, F], '--', color = 'red')
pen.highlight(A, 'A')
pen.highlight(B, 'B')
pen.highlight(C, 'C')
pen.highlight(D, 'D')
pen.highlight(P, 'P')
pen.highlight(F, 'F')
# pen.highlight_all([A, B, C, D, P, F])
pen.show()
