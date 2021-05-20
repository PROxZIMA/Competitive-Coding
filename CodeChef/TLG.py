# https://www.codechef.com/viewsolution/43728543

aScore, bScore, aLead, bLead = 0, 0, 0, 0

for _ in range(int(input())):
    a, b = map(int, input().split())

    aScore += a
    bScore += b

    lead = aScore - bScore

    if lead > 0:
        aLead = max(lead, aLead)
    else:
        bLead = max(-lead, bLead)

if aLead > bLead:
    print(1, aLead)
else:
    print(2, bLead)