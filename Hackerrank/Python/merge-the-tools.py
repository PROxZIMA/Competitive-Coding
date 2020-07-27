def merge_the_tools(string, k):
    lens = len(string)
    for i in range(0, lens, k):
        lists = [j for j in string[i:i+k]]
        print(''.join(sorted(set(lists), key=lists.index)))

s = input()
n = int(input())
merge_the_tools(s, n)