'''
Give string as input and split in to (string / k) parts after that you find the set of this substrings 
and print every substring  into newline.

'''
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(*dict.fromkeys(string[i : i + k]), sep="")
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
