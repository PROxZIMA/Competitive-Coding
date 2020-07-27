def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

s = input()
pos, char = input().split()
print(mutate_string(s, int(pos), char))