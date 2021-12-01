
from math import *
from numpy import *
def calculator(x,x1,y,y1):
    deltax=abs(x-x1)
    deltay=abs(y-y1)
    if(deltax/x>=deltay/y):
        print (x," - bilsh to4nisha nizh - ", y )
    else:
        print(y," - bilsh to4nisha nizh - ", x)
def calculator2(diff,x,gx):
    g=gx*0.001
    for n in range(10):
        if(diff<=0.5*10**(1-n+1)):
            continue
        else:
            print("n = ", n)
            break
    deltax=x*g
    print(deltax)
def calculator3(x,x1):
    deltax=0.5*0.0001
    pohibka=deltax/x
    print("deltax= ",deltax, "pohibka = ",pohibka)
    deltax1=1*0.001
    pohibka1=deltax1/x1
    print("deltax1= ",deltax1, "pohibka1 = ",pohibka1)

    
    
calculator(8.06,8.06225,1.71,1.71428)
calculator2(0.00112,72.354,0.24)
calculator3(18.275,0.00644)