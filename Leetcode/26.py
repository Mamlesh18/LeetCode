class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        dicts = {}
        for i in range(len(nums)):
            if nums[i] not in dicts:
                dicts[nums[i]] = True
                nums[k] = nums[i]
                k += 1
        return k
