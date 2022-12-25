# Format the String values 
# Here print the values of given number in binary, octal, hexadecimal, and decimal in one line with one whitespce each of the number and align the numbers with binary values   

def print_formatted(number):
    space=len(bin(number)[2:])
    for i in range(1,number+1):
        print(f"{i:>{space}} {oct(i)[2:]:>{space}} {hex(i)[2:].upper():>{space}} {bin(i)[2:]:>{space}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)        