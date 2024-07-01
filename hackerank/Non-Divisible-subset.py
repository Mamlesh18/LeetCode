def nondivisible(n,k):
    res = []
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            summing = n[i] + n[j]
            if summing % k != 0:
                c = n[i]
                d = n[j]
                res.append(c)
                res.append(d)

    visited = set(res)
    return len(visited)


n = list(map(int,input().split()))
k = int(input())
print(nondivisible(n,k))