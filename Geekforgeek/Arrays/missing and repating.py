def missrepe(nums):
    dicts = {}
    for i in nums:
        if i in dicts:
            dicts[i] +=1
        else:
            dicts[i] = 1

    result = []
    for u,v in dicts.items():
        if v > 1:
            result.append(u)
    for i in range(len(nums)):
        if i+1 not in nums:
            result.append(i+1)
    return result

nums = [1,2,2]
print(missrepe(nums))
