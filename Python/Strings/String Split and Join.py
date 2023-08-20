# Split the string and convert in to list.
# After that use join function to rearange the list in to string and return it 

def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)