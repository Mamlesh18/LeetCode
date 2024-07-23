def last(nums):
    result = []
    for i in range(0,len(nums)):
        if nums[i] == '1':
            result.append(i)
    if result:
        return max(result)
    else:
        return -1

nums = '0000'
print(last(nums))