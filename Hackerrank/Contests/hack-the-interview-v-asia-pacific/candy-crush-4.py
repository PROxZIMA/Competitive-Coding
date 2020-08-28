import re

def getMaxScore(jewels):
    l = ['aa']
    
    k = 0
    while l != []:
        l = re.findall(r'(.)\1', jewels)
        for i in l:
            jewels = jewels.replace(2*i, '', 1)
            k += 1

    return k

for _ in range(int(input())):
    jewels = input()
    print(getMaxScore(jewels))
