for _ in range(int(input())):
    preference = input().split()
    received = set(input().split())
    for company in preference:
        if company in received:
            print(company)
            break