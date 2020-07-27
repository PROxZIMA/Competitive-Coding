def sort(obj, k):
    return obj[k]

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key = lambda obj: obj[k])
    [print(' '.join(map(str, elem))) for elem in arr]
