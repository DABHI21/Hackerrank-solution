# use zeros and ones function in numpy for print array 

import numpy as np

n=list(map(int,input().split()))

print(np.zeros(n,int),sep="\n")
print(np.ones(n,int),sep="\n")
    