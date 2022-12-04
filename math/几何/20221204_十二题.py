# coding=UTF-8
from 立体几何 import 立体几何
from 立体几何 import Cube


pen  = 立体几何()
cube = Cube(2, 2, 2, reverse=True)
cube . highlight_tips(A1=' ', B1=' ', C1=' ', D1='P')
F    = (0, 0, 1)
E    = (0, 1, 1)

pen.连线([cube.A , cube.B , F      ], '--', color = 'blue')
pen.连线([cube.A , E      , cube.D1], '--', color = 'blue')
pen.连线([cube.D , cube.B , E      ], '--', color = 'green')

pen.连线([cube.B , cube.D], color = 'black')
pen.连线([cube.D1, cube.B], color = 'black')
pen.连线([cube.D1, cube.A], color = 'black')
pen.连线([cube.D1, cube.C], color = 'black')
pen.连线([cube.D1, cube.D], color = 'black')
pen.连线([cube.D1, cube.D], color = 'black')
pen.连线([cube.A , cube.B , cube.C, cube.D], color = 'black')

pen.highlight(E, 'E')
pen.highlight(F, 'F')

pen.show()
