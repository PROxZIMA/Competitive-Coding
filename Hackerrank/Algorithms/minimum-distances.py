n = int(input())
lst = input().split()

total = []
count = 0
if len(set(lst)) == n:
    print(-1)
else:
    for i in lst:
        if i in lst[count+1:]:
            total.append(lst[count+1:].index(i)+1)
        count += 1
    print(min(total))
