# Add character in string at any position 

# one way to do it 

def mutate_string(string, position, character):
    a=list(string)
    a[position]=character
    string=''.join(a)

    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Second way to do it   

def mutate_string(string, position, character):
    
    string= string[:position] + character + string[position+1:]

    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)  