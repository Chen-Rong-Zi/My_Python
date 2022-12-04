# coding = utf-8
from 立体几何 import 立体几何 


pen = 立体几何()
连线 = pen.连线
A1 = (3, 2, 0)
B1 = (3, 0, 0)
C1 = (1, 2, 0)
A  = (2, 2, 2)
B  = (2, 0, 2)
C  = (0, 2, 2)
连线([A, B, C])
连线([A1, B1, C1])
连线([A , A1])
连线([B , B1])
连线([C , C1])
连线([B , C1], color = 'red')
连线([A , C ], color = 'red')

pen.highlight(A, 'A')
pen.highlight(B, 'B')
pen.highlight(C, 'C')
pen.highlight(A1, 'A1')
pen.highlight(B1, 'B1')
pen.highlight(C1, 'C1')
pen.show()

