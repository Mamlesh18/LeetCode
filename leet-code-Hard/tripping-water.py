def rain(n):
    count = 0
    l = 0
    r = len(n) - 1
    left = n[l]
    right = n[r]
    while l < r:
        if left < right:
            l += 1
            left = max(left,n[l])
            count += left - n[l]
        else:
            r -= 1
            right = max(right,n[r])
            count += right - n[r]
    return count
n = list(map(int,input().split()))
print(rain(n))
