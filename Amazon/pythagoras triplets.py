def triplets(arr):
    for i in range(0,len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(i + 2, len(arr)):
                a = arr[i] * arr[i]
                b = arr[j] * arr[j]
                c = arr[k] * arr[k]
                if (a == b + c) or (b == a + c) or (c == a + b):
                    return True
    return False

arr = [10, 4, 6, 12, 5]
print(triplets(arr))