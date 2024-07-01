def rep(n):
    visited = []
    notvisited = []
    for i in range(0,len(n)):
        if n[i] not in visited:
            visited.append(n[i])
        else:
            notvisited.append(n[i])
    length = len(n)
    sum1 =  length * (length + 1) // 2
    a = sum(visited)
    sum2 = sum1 - a
    print("not visited".join(map(str,notvisited)))
    print("missing",sum2)


n = list(map(int,input().split()))
rep(n)