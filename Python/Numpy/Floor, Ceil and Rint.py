import numpy as np
np.set_printoptions(legacy='1.13')

A = list(map(float,input().split()))
task=[np.floor(A),np.ceil(A),np.rint(A)] 

for i in task:
    print(i)
    