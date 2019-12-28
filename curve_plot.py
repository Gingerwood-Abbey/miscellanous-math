#!/usr/bin/env python3
# referred from https://mmas.github.io/conics-matplotlib 
import matplotlib.pyplot as plt
import numpy as np
a= 4
b=2
x =np.linspace(-7,7,400)
y= np.linspace(-7,7,400)
x,y= np.meshgrid(x,y)
def axes():
    plt.axhline(0,alpha=0.1)
    plt.axvline(0,alpha=0.1)
    plt.xlabel('x')
    plt.ylabel('y')
def curve():
    #type the function as plt.contour(x,y,function)
    plt.contour(x,y,(x**2/a**2 +y**2/b**2 -1))
    plt.show()
curve()