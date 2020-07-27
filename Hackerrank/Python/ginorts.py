s = input()

small = ''
big = ''
even = ''
odd = ''

for i in s:
    try:
        if i.islower():
            small += i
        elif i.isupper():
            big += i
        elif int(i)%2 == 0:
            even += i
        elif int(i)%2 != 0:
            odd += i
    except:
        pass

print(*(sorted(small)+sorted(big)+sorted(odd)+sorted(even)), sep = '')
