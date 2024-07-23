def majority(nums):
    dicts = {}
    for i in range(len(nums)):
        if nums[i] not in dicts:
            dicts[nums[i]] = 1
        else:
            dicts[nums[i]] += 1

    max_key = max(dicts, key=dicts.get)
    return max_key

nums = [1, 2, 2, 3, 3, 3, 4]
print(majority(nums))
