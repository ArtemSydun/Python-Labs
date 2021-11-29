from scipy import integrate
from numpy import *
from math import *


def dif1(x):
    return x / (sqrt(x + 0.8))

def rt_int(rectangl, a, b, n):
    h = (b - a) / n
    rt = h * ((dif1(a)+h/2) + (dif1(b - h)+h/2))
    for i in range(1, n - 1):
        rt += dif1(a + i * h)/10
    return rt
  
def rtright_int(dif1, a, b, n):
    h = (b - a) / n
    rtright = h * (dif1(a) + dif1(b - h))
    for i in range(2, n):
        rtright += dif1(a + i * h) / 10
    return rtright

def rtleft_int(dif1, a, b, n):
    h = (b - a) / n
    rtleft = h * (dif1(a) + dif1(b - h))
    for i in range(1, n-1):
        rtleft += dif1(a + i * h) / 10
    return rtleft
 
a, err = integrate.quad(dif1, 0.6, 1.6)


def dif2(x):
    return (math.log(x**2+1) / (2*x)-1)
  
def sp_int(dif11, a, b, n):
    h = (b - a) / n
    k = 0.0
    x = a + h
    for i in range(1, n // 2 + 1):
        k += 4 * dif2(x)
        x += 2 * h

    x = a + 2 * h
    for i in range(1, n // 2):
        k += 2 * dif2(x)
        x += 2 * h
    return (h / 3) * (dif2(a) + dif2(b) + k)

b, err = integrate.quad(dif2, 1.2, 2.8)


def dif3(x):
    return x/sqrt(2+(0.5*(x**2)))

def tr_int(dif3, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (dif3(a) + dif3(b))
    for i in range(1, n):
        sum += dif3(a + i * h)
    return sum * h  
  
c, err = integrate.quad(dif3, 0.4, 1.2)


print("middle rectangle = ", rt_int(dif1, 0.6, 1.6, 10))
print("left rectangle = ", rtleft_int(dif1, 0.6, 1.6, 10))
print("right rectangle = ", rtright_int(dif1, 0.6, 1.6, 10))
print('Check for the rectangle method = ', a)

print("Trapezoid = ", tr_int(dif3, 0.4, 1.2, 20))
print('Check for trapezoid method = ', c)

print("Simpson = ", sp_int(dif2, 1.2, 2.8, 8))
print('Check for simpson method= ', b)