n = int(input())
p = int(input())

if n%2 == 0:
    front = (p-p%2)//2
    end = n//2-front
    print(min(front, end))
else:
    front = (p-p%2)//2
    end = (n-n%2)//2-front
    print(min(front, end))
