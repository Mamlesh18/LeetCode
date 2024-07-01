def binary_sorted(arr):
    n = len(arr)
    stack = []
    for i in range(0,n):
        if arr[i] == 0:
            stack.append(arr[i])
    for j in range(0,n):
        if arr[j] == 1:
            stack.append(arr[j])

    return " ".join(map(str,stack))

n = list(map(int,input().split()))
print(binary_sorted(n))

