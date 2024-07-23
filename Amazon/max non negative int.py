def maxnon(nums):
    nums.sort()
    max_ele = -1
    curr_ele = 0
    max_arr = []
    curr_arr = []
    for i in nums:
        if i >= 0:
            curr_ele+=i
            curr_arr.append(i)
        else:
            if curr_ele > max_ele:
                max_ele = curr_ele
                max_arr = curr_arr.copy()
            curr_arr = []
            curr_ele = 0
    if curr_ele > max_ele:
        max_ele = curr_ele
        max_arr = curr_arr.copy()
    return max_ele
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxnon(nums))