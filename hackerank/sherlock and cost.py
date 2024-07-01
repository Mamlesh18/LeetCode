def cost(B):
    # Write your code here
    res = []
    for i in range(len(B)-1):
        if B[i] < B[i+1]:
            c = B[i+1] - B[i]
            res.append(abs(c))
        elif B[i] >= B[i+1]:
            d = B[i] - B[i+1]
            res.append(abs(d))
    return sum(res)

n = list(map(int,input().split()))
print(cost(n))