import math
import os
import random
import re
import sys

def solve(s):
    temp=s.split(' ')
    name=''
    for i in temp:
        i=i.capitalize()
        name=name + " " + i
    name= name.replace(" ","",1)
    return name    

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()



  