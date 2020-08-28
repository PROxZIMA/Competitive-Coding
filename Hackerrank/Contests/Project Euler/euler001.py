for _ in range(int(input())):
    n = int(input())
    occ3, occ5, occ15 = (n-1)//3, (n-1)//5, (n-1)//15
    print(3*(occ3*(occ3+1))//2 + 5*(occ5*(occ5+1))//2 - 15*(occ15*(occ15+1))//2)