# coding=UTF-8
from 立体几何 import 立体几何
from 立体几何 import main

pen = 立体几何()
A = (0, 0, 0)
B = (2, 0, 0)
C = (0, 2, 0)
D = (0, 0, 2)
pen.连线([B, C, D])
pen.连线([B, A])
pen.连线([A, D])
pen.连线([A, C])

# pen.highlight_all([A, B, C, D])
# pen.show()
def tty():
    main()

tty()
