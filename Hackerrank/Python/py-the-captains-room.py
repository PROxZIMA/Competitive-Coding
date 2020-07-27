k = int(input())
rooms = input().split()

dic = {}
for room in rooms:
    dic[room] = 1 + dic.get(room, 0)

for key, value in dic.items():
    if value == 1:
        print(key)
