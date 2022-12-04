# coding=UTF-8
from 立体几何 import 立体几何
from 立体几何 import Cube


pen = 立体几何()
pen.axis.set_title('cube')

cube = Cube(20, 20, 20, reserve=True)
cube.show_tips()
cube.plot()

pen.连线([cube.A , cube.C], '--', color='red')
pen.连线([cube.D1, cube.B], '--', color='red')
pen.连线([cube.A1, cube.D], '--', color='red')
pen.连线([cube.B1, cube.D], '--', color='green')
pen.show()
