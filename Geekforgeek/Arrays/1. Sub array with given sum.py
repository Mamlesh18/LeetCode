def sub(nums,k):
    left = 0
    right = 0
    current = 0
    while right < len(nums):
        current += nums[right]
        while current > k and left < right:
            current-=nums[left]
            left+=1

        if current == k:
            return left,right
        right+=1

    return None

nums = [1,2,3,7,5]
k = 12
print(sub(nums,k))
