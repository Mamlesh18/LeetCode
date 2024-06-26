class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        count = 0
        result = 0
        a = 0
        for i in range(len(nums)-1):
            a = max(a, i+nums[i])
            if i==count:
                result +=1
                count = a
                if count >= len(nums) - 1:
                    break

        return result

