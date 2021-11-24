import numpy as np
from numpy import *
from math import *
from matplotlib.pyplot import *
from sympy import *
def taylor(x):
  y=0
  d1=diff(f,x)
  d2=diff(d1,x)
  d3=diff(d2,x)
  d4=diff(d3,x)
  print('d1=',d1,'d2=',d2,'d3=',d3,'d4=',d4)
  y+=f +d1*x + d2*(x-0)**2/2+d3*(x-0)**3/6+d4*(x-0)**4/24
  print ('y=',y)
  return y
x=symbols('x')
f=sin(4*x)
taylor_x=taylor(x)
plt=plot(f,taylor_x,(x,-1,1), label='Taylor')

title('LB11 V. 7 Sydun')
legend(loc='upper right')
xlabel('х')
ylabel('y')
grid()
