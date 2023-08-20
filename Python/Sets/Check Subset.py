# A is subset of B 

i=int(input())

for d in range(i):
    x=int(input())
    a=set(map(int,input().split()))
    y=int(input())
    b=set(map(int,input().split()))

    if set(a.intersection(b))==set(a):
        print("True")
    else:
        print("False")



