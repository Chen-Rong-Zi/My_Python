# coding=UTF-8
from 立体几何 import 立体几何



pen = 立体几何()
B = (0, 0, 0)
C = (2, 0, 0)
D = (0, 3, 0)
B1 = (0, 0, 4)
C1 = (2, 0, 4)
D1 = (0, 3, 4)
E = (0, 1.6, 2)
O = (1, 1.5, 2)
pen.连线([B, C, D])
pen.连线([D1, B])
pen.连线([D1, C])
pen.连线([B1, C1, D1])
pen.连线([B, B1])
pen.连线([C, C1])
pen.连线([D, D1])
pen.连线([D, E, O], '--', color='red')
pen.show()


