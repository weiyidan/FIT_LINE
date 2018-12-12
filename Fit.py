######################################################
###### Written by Yidan Wei ##########################
###### Address: 272918553@qq.com #####################
###### If any bug exists, contact me #################
######################################################

#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


#直线方程函数
def f_1(x, A, B):
    return A*x + B
 
#二次曲线方程
def f_2(x, A, B, C):
    return A*x*x + B*x + C
 
#三次曲线方程
def f_3(x, A, B, C, D):
    return A*x*x*x + B*x*x + C*x + D

#高斯曲线方程
def f_gauss(x, A, B, C, sigma):
    return A*np.exp(-(x-B)**2/(2*sigma**2)) + C
 
#拟合点
str_x = input('x:')
x0 = [int(n) for n in str_x.split()]
str_y = input('y:')
y0 = [int(n) for n in str_y.split()]
 
print(x0)

#绘制散点
plt.scatter(x0[:],y0[:], 25, "red")
 
#直线拟合与绘制
A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]
x1 = np.arange(0, 6, 0.01)
y1 = A1*x1 + B1
plt.plot(x1, y1, "blue")
 
#二次曲线拟合与绘制
A2, B2, C2 = optimize.curve_fit(f_2, x0, y0)[0]
x2 = np.arange(0, 6, 0.01)
y2 = A2*x2*x2 + B2*x2 + C2 
plt.plot(x2, y2, "green")
 
#三次曲线拟合与绘制
A3, B3, C3, D3= optimize.curve_fit(f_3, x0, y0)[0]
x3 = np.arange(0, 6, 0.01)
y3 = A3*x3*x3*x3 + B3*x3*x3 + C3*x3 + D3 
plt.plot(x3, y3, "purple")
 
#高斯曲线方程
A4, B4, C4, SIGMA= optimize.curve_fit(f_gauss, x0, y0)[0]
x4 = np.arange(0, 6, 0.01)
y4 = A4*np.exp(-(x4-B4)**2/(2*SIGMA**2)) + C4
plt.plot(x4, y4, "black")

plt.title("test")
plt.xlabel('x')
plt.ylabel('y')
 
plt.show()
