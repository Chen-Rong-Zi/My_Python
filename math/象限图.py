# coding = UTF-8
import matplotlib.pyplot as plt
from 标准几何.立方体 import 立方体 as 立方体
from 标准几何.三角锥 import 三角锥 as 三角锥



fig  = plt.figure()
fig.suptitle('python!')

cube = 立方体(111, 9, 9, 9, border = 0.5)
cube.show_tips()    # 标注立方体顶点

tri  = 三角锥(111, 3, 6, 9, mode = '直角棱锥')
trg  = plt.plot([1.5, 9], [3, 9], [0, 9], color ='red')




if __name__ == '__main__':
    plt.show()

