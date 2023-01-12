# Give array as input and print it using numpy library
  
import numpy

def arrays(arr):
    a=numpy.array(arr,float)
    return a[::-1]
arr=input().strip().split(" ")
result=arrays(arr)
print(result)    