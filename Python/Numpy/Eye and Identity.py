import numpy as np
np.set_printoptions(legacy='1.13')

n=list(map(int,input().split()))

print(np.eye(*tuple(n)))
