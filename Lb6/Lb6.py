

import numpy as np
print("Method of Gauss")
a = np.matrix([ [1,1,-1], [3, -1, 2], [4, 4, -3] ])
b = np.matrix([[-2], [9], [-5]])
print ("Matrix A = ", a)
print ("\nMatrix b = ", b)

def fun():    
    k = 1
    n = len(b)
    while k<=n-1:
        i = k+1
        while i<n:
            if a[i,k]!=0.0:
                a[i,k+1:n] = a[i,k+1:n] - (a[i,k]/a[k,k])*a[k,k+1:n]
                b[i] = b[i] - (a[i,k]/a[k,k])*b[k]
            i += 1
        k += 1
    k = n-1
    while k > -1:
        b[k] = (b[k] - np.dot(a[k,k+1:n], b[k+1:n]))/a[k,k]
        k-=1
    return b
print ("\nGauss: ", fun())
    
print("\nCheck of solution of Method of Gauss: ", np.linalg.solve(a,b))

print("\nGauss-Jordan Method", np.linalg.inv(a)*b)
