from collections import deque

s = input()

def received(s):
    nk = True
    deq = deque([])
    index = 0
    for i in s:
        if i == '#':
            nk = not(nk)
        elif i == '<':
            index = 0
        elif i == '>':
            index = len(deq)
        elif i == '*':
            if index == 0:
                continue
            else:
                deq[index-1] = ''
                index -= 1
        else:
            if i.isdigit() and not(nk):
                continue
            else:
                deq.insert(index, i)
                index += 1

    return ''.join(deq)

result = received(s)

print(result)
