# swap cases: In any string convert words in Upper case to Lower case and print it.

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
