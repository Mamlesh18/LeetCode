def copy(m):
    # return " ".join(map(str,reversed(m)))
    a = []
    for i in range(len(m) - 1, -1, -1):
        a.append(m[i])
    return " ".join(map(str,a))

t = int(input())
for _ in range(t):
    num = int(input())
    ele = list(map(int,input().split()))
    print(copy(ele))
