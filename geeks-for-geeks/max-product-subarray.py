def max_product(n):
    if len(n) == 0:
        return None

    result = n[0]
    for i in range(0,len(n)):
        a = n[i]
        for j in range(i+1,len(n)):
            result = max(result,a)
            a *= n[j]
        result = max(result,a)
    return result


n = list(map(int,input().split()))

print(max_product(n))