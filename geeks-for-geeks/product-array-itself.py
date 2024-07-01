def product(n):
    if len(n) == 0:
        return None

    output = [1] * len(n)

    left = 1
    right = 1
    for i in range(len(n)):
        output[i] *= left
        left *= n[i]

    for i in range(len(n)-1,-1,-1):
        output[i] *= right
        right *= n[i]

    return " ".join(map(str,output))


n = list(map(int,input().split()))

print(product(n))