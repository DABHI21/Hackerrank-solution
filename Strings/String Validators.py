# use "any" function which is return the boolean value for any condition in loop or iteration 
if __name__ == '__main__':
    s = input()

    a= any(i.isalnum() for i in s)
    b= any(i.isalpha() for i in s)
    c= any(i.isdigit() for i in s)
    d= any(i.islower() for i in s)
    e= any(i.isupper() for i in s)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)