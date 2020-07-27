num, lis = int(input()), input().split()
print(bool(all((int(i)>0 for i in lis)) and any((i[::-1] == i for i in lis))))
