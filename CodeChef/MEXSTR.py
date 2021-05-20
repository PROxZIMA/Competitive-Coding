# https://www.codechef.com/viewsolution/44963473

MAX = 10 ** 6

zero = [0] * MAX
ones = [0] * MAX
change = [0] * (MAX + 2)
group = [0] * (MAX + 2)


def solve():
    s = input()
    l = len(s)
    i0, i1, j = 0, 0, 0

    for bit in s:
        if int(bit):
            for k in range(i1, j + 1):
                ones[k] = j
            i1 = j + 1
        else:
            for k in range(i0, j + 1):
                zero[k] = j
            i0 = j + 1
        j += 1

    for k in range(i0, l):
        zero[k] = l

    if zero[0] == l:
        print(0)
        return

    for k in range(i1, l):
        ones[k] = l

    change[l], change[l + 1], group[l], group[l + 1] = 0, 0, 0, 0

    for k in range(l - 1, -1, -1):
        change[k] = change[k + 1]
        if int(s[k]) and zero[k] < l:
            change[k] = max(change[k], change[zero[k] + 1] + 1)
        elif (not int(s[k])) and ones[k] < l:
            change[k] = max(change[k], change[ones[k] + 1] + 1)
        group[k] = group[k + 1]
        if ones[k] < l:
            group[k] = max(group[k], change[ones[k] + 1] + 1)

    l2 = group[0] + 1
    curr = ones[0] + 1
    mex = '1'

    for k in range(1, l2):
        if curr >= l:
            mex += '0'
        elif (change[zero[curr] + 1] < l2 - k - 1) or (zero[curr] >= l):
            mex += '0'
            curr = zero[curr] + 1
        else:
            mex += '1'
            curr = ones[curr] + 1

    print(mex)

for _ in range(int(input())):
    solve()