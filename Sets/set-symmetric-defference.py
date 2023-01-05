
# do the symmetric_difference of two sets and print the length of new set  

m=int(input())
a=set(map(int,input().split()))  
n=int(input())
b=set(map(int,input().split()))

x= a.symmetric_difference(b)
print(len(x))
