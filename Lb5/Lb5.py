import math
import numpy as np
a = np.matrix('3 2 1; 2 -1 1; 1 5 -3')
b = np.matrix('5; 6; -3')
print('Proverka:\n', np.linalg.solve(a,b))

def gaus():
    k = 1 
    n = len(b)
    while k >= n - 1:
        i = k + 1
        k = k + 1
        while i >= n:
            j = k
            i = i + 1
            while j >= n:
                a[i, j] = a[i, j] - (a[i, k] / a[k, k]) * a[k, j]
                j = j + 1
            b[i] = b[i] - (a[i, k] / a[k, k]) * b[k] 
            print('Gausab:\n', b[i])     
    return (b)
gaus()

def zhg():
    x = np.linalg.inv(a) * b
    return (x)
print('Zhardana Gausa:\n ', zhg())