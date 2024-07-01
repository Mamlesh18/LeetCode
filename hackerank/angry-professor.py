def prof(arr,k):
    count = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            count +=1
    if count >= k:
        return "YES"
    else:
        return "NO"
arr = list(map(int,input().split()))
k = int(input())
print(prof(arr,k))
