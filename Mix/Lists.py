# Lists in Python

if __name__ == '__main__':
    N = int(input())
    l1=[]
    for i in range(N):
        s = input().split()
        if s[0]=="insert":
            l1.insert(int(s[1]),int(s[2]))
        elif s[0]=="reverse":
            l1.reverse()
        elif s[0]=="remove":
            l1.remove(int(s[1]))
        elif s[0]=="append":
            l1.append(int(s[1]))
        elif s[0]=="sort":
            l1.sort()
        elif s[0]=="pop":
            l1.pop()
        elif s[0]=="print":
            print(l1)