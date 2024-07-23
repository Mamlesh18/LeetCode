def kth(nums,k):
    if not nums:
        return []
    if len(nums) < k:
        return -1

    a = k-1
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]

    return nums[k-1]
nums = [7,10,4,3,20,15]
print(kth(nums,3))