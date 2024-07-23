def small(nums):
    res = 1
    for i in range(0,len(nums)):
        if nums[i] <= res:
            res+= nums[i]
    return res
arr = [1,1,3,4]
print(small(arr))