n=int(input())
stamps=[]
for i in range(n):
    stamps.append(input())
print(stamps)    
flags=set(stamps)
print(len(flags))
