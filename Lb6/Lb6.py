import math
from scipy import optimize
x0 = 3.4
y0 = 1.3
def f1(x):
    return 0.5 - math.cos(x-1)
def f2(y): 
    return 3 + math.cos(y)
def iter (x, y, e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1 - xn) >= e) & (abs(yn1 - yn) >= e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn1)
        n += 1 
    print ('Simple iteration:')
    print ('x1=', xn, '\ny1=', yn, '\nnumber of iteration = ', n)
iter (x0, y0, 0.0001)
def f(x):
    return math.cos(x[0]-1) + x[1] - 0.5, x[0] - math.cos(x[1])-3
s = optimize.root (f, [0,0], method = 'hybr')
print (s.x)