import math

def cube(N):
    count = 0
    for i in range(1, int(math.pow(N, 1 / 3) + 1)):
        cb = i * i * i
        diff = N - cb
        cbrtDiff = int(math.pow(diff, 1 / 3))
        if (cbrtDiff * cbrtDiff * cbrtDiff == diff):
            count += 1
    return count


t = int(input())
for i in range(t):
    n = int(input("element "))
    print(cube(n))