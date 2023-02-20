from itertools import combinations

s,k = input().strip().split()
s = sorted(s)
for i in range(1,int(k)+1):
    ls = list(combinations(s,int(i))) 
    for x in ls:
        print("".join(x))