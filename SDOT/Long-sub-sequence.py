def longsub(nums):
    n = len(nums)
    stack = [1]*n
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:

                stack[i] = max(stack[i],stack[j] + 1)
    return max(stack)




nums = list(map(int,input().split()))
print(longsub(nums))