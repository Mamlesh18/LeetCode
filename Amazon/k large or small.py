def kth(arr,k):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr[-k:]

arr = [1,23,2,4,566,4,389,42]
k = 3
print(kth(arr,k))