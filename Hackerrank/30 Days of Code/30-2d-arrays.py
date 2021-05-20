arr = [list(map(int, input().split())) for _ in range(6)]
maxi = -37

for i in range(4):
    for j in range(4):
        hgsum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

        if maxi < hgsum:
            maxi = hgsum

print(maxi)