def hurdle(arr,k):

    stack = []

    for i in range(len(arr)):
        if arr[i] > k:
            b = arr[i] - k
            stack.append(b)
    return max(stack)

arr = list(map(int,input().split()))
k = int(input())
print(hurdle(arr,k))