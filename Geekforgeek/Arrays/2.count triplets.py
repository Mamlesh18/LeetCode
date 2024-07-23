def triplets(nums):
    count = 0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] in nums:
                count+=1
    return count

arr = [1,5,3,2]
print(triplets(arr))