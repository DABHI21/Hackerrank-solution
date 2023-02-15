from itertools import combinations

A,x= list(map(str,input().split()))
# word=sorted(list(combinations(A,len(A)>=int(x))))
# for i in word:
#     print(''.join(i))
    
words=sorted(list(combinations(A,int(x)))) 
print(words)
# for i in words:
#     print(''.join(i))