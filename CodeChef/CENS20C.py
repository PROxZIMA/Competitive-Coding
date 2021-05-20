# https://www.codechef.com/viewsolution/37925734

def search(arr, lenl, val):
    s = 0
    l = lenl - 1

    total = 0

    while (s <= l):
        m = int((s + l) / 2)

        if (arr[m] <= val):
            total = m + 1
            s = m + 1

        else:
            l = m - 1

    return total


def kmpsearch(string, lps):
    lis = []
    lens = len(string)
    lensh = lens // 2

    l = 0
    i = 0
    while i < lens:
        if string[i] == pat[l]:
            l += 1
            i += 1
        elif l > 0:
            l = lps[l - 1]
        else:
            i += 1

        if l == lenp:
            if i - l < lensh:
                lis.append(i - l)

            l = lps[l - 1]

    return lis


def kmp(pat, lenp):

    lps = [0]*(lenp)
    l = 0
    i = 1

    while i < lenp:
        if pat[i] == pat[l]:
            l += 1
            lps[i] = l
            i += 1
        elif l > 0:
            l = lps[l-1]
        else:
            lps[i] = 0
            i += 1

    return lps



keyword = input()
pat = input()
q = int(input())

lenk = len(keyword)
lenp = len(pat)

k = keyword * 2
lis = kmpsearch(k, kmp(pat, lenp))
lenl = len(lis)

for _ in range(q):
    n = int(input())
    count = 0

    q = n // lenk
    r = n % lenk

    count += search(lis, lenl, r - lenp)

    if q >= 1:
        count += search(lis, lenl, lenk + r - lenp)

    if q >= 2:
        count += (q - 1)*lenl

    print(count)