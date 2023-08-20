A=list(map(int,input().split()))
n=int(input())
for i in range(n):
    o=list(map(int,input().split()))
if A is o :
    print(False)
elif o in A:
    print(True)
else:
    print(False)