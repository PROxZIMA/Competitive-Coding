T = int(input())
for i in range(T):
    lena, seta = int(input()), set(map(int, input().split()))
    lenb, setb = int(input()), set(map(int, input().split()))
    print(seta.issubset(setb))
