student_marks = {}
for _ in range(int(input())):
    name, *marks = input().split()
    scores = list(map(float, marks))
    student_marks[name] = scores
query_name = input()
print(f'{sum(student_marks[query_name])/3:.2f}')
