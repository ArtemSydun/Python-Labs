import matplotlib.pyplot as plt
import numpy as np
x = np.array([0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5])
y = np.array([1.62, 1.98, 2.32, 2.71, 2.48, 1.82, 1.15, 0.70, 2.04, 1.82])
x1 = sum(x)/10
x2 = sum(x**2)/10
y1 = sum(y)/10
yx = sum(x*y)/10
a1 = (yx - x1*y1)/(x2 - x1**2)
a0 = y1 - a1 * x1
x_graph = np.array([-1 , 1])
y_graph = np.array([0.5,2.5])
plt.plot( x,y,x_graph , y_graph)
plt.title("Sydun LB12 Variant 5")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()