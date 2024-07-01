def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    sum1 = 0
    sum2 = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            sum1 += nums[i]
        else:
            sum2+= nums[i]
    return max(sum1,sum2)

nums = list(map(int,input().split()))
print(rob(nums))


