import numpy as np

N, M = map(int,input().split())
A = np.array([input().split() for _ in range(N)], int)

print(np.mean(A,axis=1))
print(np.var(A,axis=0))
print(np.round(np.std(A),decimals=11))