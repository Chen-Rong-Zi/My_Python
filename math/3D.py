import numpy as np
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt

x = [0,   0,   4,   0,   5]
y = [0,   0,   0,   4,   5]
z = [0,   0,   0,   0,   0]

# 遍历每一个点, 做它与其他各点的连线
ax=plt.subplot(111, projection='3d')
for i in range(len(x)):
    for j in range(len(y)):
        ax.plot((x[i],x[j]), 
                (y[i],y[j]), 
                (z[i],z[j]), color='red')

for i in range(len(x)):
    ax.text(x[i],y[i],z[i],i,color='blue')


ax.set_zlabel('z')
ax.set_ylabel('y')
ax.set_xlabel('x')
plt.show()
