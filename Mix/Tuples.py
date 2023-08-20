# Basic Data type code for tuples

"""
You run This code in Pypy3 for HackerRank
If you run in python 3 than you got nagetive output so run in Pypy3.

"""
 

if __name__== '__main__':
    n=int(input())
    l1=input()
    t=tuple(map(int,l1.split(" ")))
    print(hash(t))
