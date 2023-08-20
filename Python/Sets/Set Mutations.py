
n , s = int(input()), set(map(int, input().split()))

for x in range(int(input())):
    eval(f"s.{input().split()[0]}(set(map(int, input().split())))")
   
print(sum(s))
