
"""
Get the user input of the set and remove the elements from the set acording to given arguments
 
"""

n = int(input())
s = set(map(int, input().split()))
x=int(input())
for i in range(x):
    command=input()
    if len(command)==3:
        s.pop()
    elif len(command)==8:
        s.remove(int(command[-1]))
    elif len(command)==9:
        s.discard(int(command[-1]))
print(sum(s))                
   