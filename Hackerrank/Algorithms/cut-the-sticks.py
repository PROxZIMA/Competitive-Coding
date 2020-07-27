n = int(input())
arr = list(map(int, input().split()))

while True:
    print(len(arr))
    mini = min(arr)
    arr = [i-mini for i in arr if i-mini>0]
    if arr == []:
        break
