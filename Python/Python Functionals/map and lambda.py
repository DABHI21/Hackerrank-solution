cube = lambda x: int(x**3)   # complete the lambda function 

def fibonacci(n):
    fib = []
    for i in range(n):
        if(i == 0):
            x = 0
            fib.append(x)
        elif(i == 1):
            x = 1
            fib.append(x)
        else:
            x = fib[i - 1] + fib[i - 2]
            fib.append(x)
    return fib  
           
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n)))) 