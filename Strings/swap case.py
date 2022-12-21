# swap cases: In any string convert letters in Upper case to Lower case and vice versa.

def swap_case(s):
    a=''
    for i in s:
        if i.islower():
            i=i.upper()
        else:
            i=i.lower()
        a +="".join(i)        
    return a

if __name__ == '__main__':
    s = input()         
    result = swap_case(s)
    print(result)
