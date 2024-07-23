def next(nums):
    result = []
    for i in range(0,len(nums),1):
        next = -1
        for j in range(i+1,len(nums),1):
            if nums[i] < nums[j]:
                next = nums[j]
                break
        result.append(next)
    return result
nums = [4,5,2,25]
print(next(nums))