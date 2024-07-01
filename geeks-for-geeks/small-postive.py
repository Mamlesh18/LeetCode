def small(n):
    count = 1
    for i in range(len(n)):
        if n[i] <= count:
            count += n[i]
        else:
            break
    print(count)
n = list(map(int,input().split()))
small(n)