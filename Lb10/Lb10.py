
from numpy import *
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
x = [0.6,0.9,1.3,1.8,2.2]
y = [0.53,1.68,3.65,2.13,4.37]
spl= UnivariateSpline(x,y)
xs = linspace(0.6,2.2,500)
plt.plot(x,y,'ro',xs,spl(xs),'g')
plt.title('LB10')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

