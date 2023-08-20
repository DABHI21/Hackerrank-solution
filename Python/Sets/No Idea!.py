# count the happiness 

# method 1 for solve this Problem 

# m=input()
# n=input().split()
# a=input().split()
# b=input().split()
# hep=0
# for i in n:
#     if i in a :
#         hep+=1
#     if i in b:
#         hep-=1
# print(hep) 


# If you got time related error then you refere this code 
# second method for this problem 

num=input().split()
l=input().split() 
happiness=set(input().split()) 
Not_happy=set(input().split())

print(sum((i in happiness ) - (i in Not_happy) for i in l))

