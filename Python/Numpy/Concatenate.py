import numpy as np
"""
we can solve this problem using 2 ways 
one using concatenate and one is without concatenate

"""
# Way1 : without use of concatenate

# n,m,p=list(map(int,input().split()))
# arr=np.array([list(map(int,input().split())) for i in range(n+m)])
# print(arr)

# way2 : using concatenate

n,m,p=list(map(int,input().split()))
arr1=np.array([list(map(int,input().split())) for i in range(n)])
arr2=np.array([list(map(int,input().split())) for j in range(m)])
print(np.concatenate((arr1,arr2),axis=0))


    