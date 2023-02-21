N, M = input().split()
N = int(N)
M = int(M)
    
for value in range(0,N):
    for  inner_value in range(0,M):
        if value < int(N/2):
            if inner_value < ((M-3)/2 - value*3):
                print('-',end="")
            elif inner_value >= ((M-3)/2 + 3 + value*3):
                print('-',end="")
            elif (inner_value-1)%3==0:
                print("|",end="")
            else:
                print(".",end="")
        elif value > int(N/2):
            if inner_value < ((M-3)/2 - (N-value-1)*3):
                print('-',end="")
            elif inner_value >= ((M-3)/2 + 3 + (N-value-1)*3):
                print('-',end="")
            elif (inner_value-1)%3==0:
                print("|",end="")
            else:
                print(".",end="")
        else:
            print("-"*int((M-7)/2)+"WELCOME"+"-"*int((M-7)/2),end="")
            break
    print("")
