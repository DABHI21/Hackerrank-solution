# Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()
    for i in range(0,len(arr)):
         if arr[i] < max(arr):
            print(arr[i])
            break 