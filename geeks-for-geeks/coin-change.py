def coin(n, k):
    count = [0] * (k + 1)
    count[0] = 1
    for i in n:
        for j in range(i, k + 1):
            count[j] += count[j - i]
            print(count[j])
    print(count[k])

n = list(map(int, input().split()))
k = int(input())
coin(n, k)
