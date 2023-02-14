from itertools import permutations

A,x= list(map(str,input().split()))

words=sorted(list(permutations(A,int(x))))
for i in words:
    print(''.join(i))
    