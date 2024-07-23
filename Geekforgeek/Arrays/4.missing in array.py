def missing(nums):
    for i in range(len(nums)+1):
        if i+1 not in nums:
            return i+1
nums = [1]
print(missing(nums))