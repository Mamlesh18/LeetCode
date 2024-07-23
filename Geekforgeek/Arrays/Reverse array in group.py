def reverse(nums,k):
    if k > len(nums):
        return nums[::-1]

    result = nums[:k]
    a = result[::-1]
    b = nums[k:]
    b = b[::-1]
    return a + b
nums = [5, 6, 8, 9]
k = 5
print(reverse(nums,k))