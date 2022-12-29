def average(array):
    sets=set(array)
    s=sum(sets)
    length=len(sets)
    ave = s/length
    return ave

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)