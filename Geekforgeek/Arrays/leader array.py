def leader(nums):
    leader = list()
    count = 0
    while len(nums)>0:
        maxi = max(nums)
        leader.append(maxi)
        index = nums.index(maxi)
        nums = nums[index+1:]
        count+=1
    return leader,count
nums = [6,7,4,3,5,2]
print(leader(nums))