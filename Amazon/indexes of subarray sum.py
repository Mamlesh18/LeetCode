def subArraySum(arr,s):
    left = 0
    right = 0
    current  = 0
    while right < len(arr):
        current += arr[right]
        while current > s and left <= right:
            current-=arr[left]
            left+=1

        if current==s:
            return left,right
        right+=1
    return None

arr = [1,2,3,7,5]
s = 12
print(subArraySum(arr,s))
