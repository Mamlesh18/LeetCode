def kadane(nums):
    maximum = nums[0]
    currsum = 0
    for i in nums:
        if currsum < 0:
            currsum = 0
        currsum+=i
        maximum = max(currsum,maximum)
    return maximum


nums = [-3,-1,-1]
print(kadane(nums))
