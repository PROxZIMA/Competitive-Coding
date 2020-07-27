from datetime import datetime
date_format = "%d %m %Y"
a = datetime.strptime(input(), date_format)
b = datetime.strptime(input(), date_format)
delta = a - b
if delta.days<=0:
    print(0)
elif a.year != b.year:
    print((a.year-b.year) * 10000)
elif a.month != b.month:
    print((a.month-b.month) * 500)
elif a.day != b.day:
    print((a.day-b.day) * 15)
