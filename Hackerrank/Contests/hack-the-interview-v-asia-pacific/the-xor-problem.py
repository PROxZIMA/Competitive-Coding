def maxXorValue(s, k):
    y = ''
    for i in s:
        if k > 0:
            if i == '1':
                y += '0'
            else:
                y += '1'
                k -= 1
        else:
            break
        
    return y.ljust(len(s), '0')


for t_itr in range(int(input())):
    s = input()
    k = int(input())

    print(maxXorValue(s, k))