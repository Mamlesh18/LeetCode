def peak(nums):
    n  = len(nums)
    if n == 1:
        return 0
    if n == 2:
        return 0 if nums[0] > nums[1] else 1
    for i in range(1,len(nums)-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return i

    if nums[0] > nums[1]:
        return 0

    if nums[n-1] > nums[n-2]:
        return n-1

nums = [10, 20, 15, 2, 23, 90, 67]
print(peak(nums))