def small(nums):
    for i in range(1,len(nums)-1):
        if nums[i] > nums[i-1] and nums[i] < nums[i+1]:
            return nums[i]
    return -1

nums = [11,9,12 ]
print(small(nums))