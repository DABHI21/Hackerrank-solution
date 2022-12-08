import math
import os
import random
import re
import sys


n = int(input().strip())
if  n%2 !=0 or 6 <= n <= 20 :
    print("Weird")
elif (n%2==0) or n>20 :
    print("Not Weird")