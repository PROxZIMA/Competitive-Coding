def split_and_join(line):
    return '-'.join(line.split())
    # return line.replace(' ', '-')

s = input()
print(split_and_join(s))