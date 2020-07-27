def print_rangoli(size):
    string = ''
    for i in range(97+size-1, 96, -1):
        print((string+chr(i)+string[::-1]).center(4*size-3, '-'))
        string+=chr(i)+'-'
    for i in range(2, 2*size, 2):
        print((string[:-i]+string[:-i-3][::-1]).center(4*size-3, '-'))

num = int(input())
print_rangoli(num)