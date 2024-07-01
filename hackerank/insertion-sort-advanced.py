def insertion(n):
    count = 0

    if n == sorted(n):
        return 0
    else:
        for i in range(len(n) - 1):
            for j in range(i + 1, len(n)):
                if n[i] >= n[j]:
                    n[i], n[j] = n[j], n[i]
                    count += 1
    return n

n = list(map(int,input().split()))
print(insertion(n))