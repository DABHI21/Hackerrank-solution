a=int(input())
s = set(map(int, input().split()))
b=int(input())
n=set(map(int,input().split()))

x=s&n
print(len(x))