
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from math import *
def example1(x, y):
    return x + sin(y/sqrt(0.7))
def Ejler(example1, x, y):
    h = 0.2
    x = 1.2
    y = 1.4
    xmas = ([])
    ymas = ([])
    for i in range (6):
      x += h
      xmas.append([x])
      y += h* example1(x, y)
      ymas.append([y])
    plt.subplot(221)
    plt.title('Ejler')
    plt.plot(xmas, ymas)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    print("x by Ejler",xmas,"\ny by Ejler\n",ymas)
def example2(x, y):
    return x + sin(y/sqrt(11))

def EjlerKoshi(euler_coshi, x, y):
    h = 0.2
    x = 0.6
    y = 1.2
    xmas = ([])
    ymas = ([])
    for i in range (6):
        x += h
        xmas.append([x])
       
        y += h/2 * (example2(x, y) + example2(x+h, example2(x, y)))
        ymas.append([y])
    plt.subplot(222)
    plt.title('Koshi')
    plt.plot(xmas, ymas)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    print("x by EjlerKoshi",xmas,"\ny by EjlerKoshi\n",ymas)
print(Ejler(example1, 1.2, 2.2))
print(EjlerKoshi(example2, 0.6, 1.6))

