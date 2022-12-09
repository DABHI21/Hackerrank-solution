import re

n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    i = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if i:
        print(x,y)