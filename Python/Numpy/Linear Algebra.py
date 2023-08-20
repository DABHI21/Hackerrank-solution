import numpy as np
N=int(input())
a=np.array([input().split() for i in range(N)],dtype='f')

print(round(np.linalg.det(a),2))