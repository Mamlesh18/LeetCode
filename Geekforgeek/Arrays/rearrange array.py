def reaarane(nums):
    left = 0
    right = len(nums)-1
    result = []

    while left < right:
        if len(nums) % 2 != 0:
            result.append(nums[right])
            result.append(nums[left])
        else:
            result.append(nums[right])
            result.append(nums[left])
        left +=1
        right-=1

    if len(nums) % 2 !=0:
        mid = (left+right)//2
        result.append(nums[mid])

    return result

nums = [1,2,3,4,5,6,7]
print(reaarane(nums))