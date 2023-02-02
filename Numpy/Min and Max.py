import numpy as np

N, M = map(int,input().split())
A = np.array([input().split() for _ in range(N)], int)

x= np.min(A,axis=1)
print(max(x))