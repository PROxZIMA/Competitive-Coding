# https://www.codechef.com/viewsolution/35871836

s = ''
for i in range(int(input())):
    n = int(input())
    s += 'O' + (n-1)*'.' + (64-n)*'X'

for i in range(0, len(s)-7, 8):
    print(s[i:(i+8)])