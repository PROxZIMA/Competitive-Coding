from datetime import datetime as dt

for _ in range(int(input())):
    s = '%a %d %b %Y %H:%M:%S %z'
    t1_obj = dt.strptime(input(), s)
    t2_obj = dt.strptime(input(), s)
    print(abs(int((t1_obj - t2_obj).total_seconds())))
