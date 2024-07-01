def producr(n):
    value = [1] * len(n)
    left = 1
    right = 1

    for i in range(len(n)):
        value[i] *= left
        left *= n[i]


    for i in range(len(n) -1,-1,-1):
        value[i] *= right
        right *= n[i]
    return value

t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    print(producr(li))
