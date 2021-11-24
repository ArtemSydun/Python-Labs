from numpy import *
import numpy as np
import matplotlib.pyplot as plt
def sd(x):
    return 8*sin(x)*sin(2*x)/x**0.5
x = linspace(1, 10, 8)
y = sd(x)
plt.plot(x, y, 'g--', label='8*sin(x)*sin(2*x)/(x**(1/2))')
plt.title('Sydun Lab7')
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

