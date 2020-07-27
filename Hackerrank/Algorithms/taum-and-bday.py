for _ in range(int(input())):
    b, w = map(int, input().split())
    bc, wc, z = map(int, input().split())
    if bc > wc + z:
        print(((b + w) * wc) + (b * z))
    elif wc > bc + z:
        print(((b + w) * bc) + (w * z))
    else:
        print((b * bc) + (w * wc))
