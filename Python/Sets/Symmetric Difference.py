"""
input two sets from user and get the symmetric defference of the given sets. Print every integer in new line.

"""
m=int(input())
a=set(map(int,input().split()))  
n=int(input())
b=set(map(int,input().split()))

i = a.union(b) 
j= a.intersection(b)

for x in sorted(i.difference(j)):
    print(x)









