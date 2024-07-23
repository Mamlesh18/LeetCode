def equi(nums):
    if len(nums) == 1:
        return nums

    result_left = [0] * len(nums)
    result_right = [0] * len(nums)
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            result_left[i]+= nums[j]
    for i in range(len(nums)):
        for j in range(i):
            result_right[i]+= nums[j]


    for i in range(0,len(result_right)):
        if result_right[i] == result_left[i]:
            return result_right[i]

nums = [1]
print(equi(nums))