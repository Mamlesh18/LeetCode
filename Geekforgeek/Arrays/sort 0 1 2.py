def sorti(nums):
    zeros = []
    ones = []
    two = []
    for i in nums:
        if i == 0:
            zeros.append(i)
        elif i == 1:
            ones.append(i)
        elif i == 2:
            two.append(i)
    return zeros + ones + two

nums = [0,2,1,2,0]
print(sorti(nums))