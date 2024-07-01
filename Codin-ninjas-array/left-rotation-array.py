def left_rotate(n,k):

    length = len(n)
    for i in range(0, len(k)):
        k[i] = k[i] % length
        rota = n[k[i]:] + n[:k[i]]
        print(" ".join(map(str,rota)))
        return 1






t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    li = list(map(int,input().split()))
    rot = list(map(int,input().split()))
    print(left_rotate(li,rot))



