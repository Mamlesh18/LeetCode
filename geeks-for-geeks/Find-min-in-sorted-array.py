def sorted(n):

    if len(n) <= 1:
        return n
    arr = n[0]
    for i in range(0,len(n)):
        if n[i] < arr:
            arr = n[i]
    return arr

num = list(map(int,input().split()))

print(sorted(num))