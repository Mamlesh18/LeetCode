class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        count = 0

        for i in range(0, len(nums) - 1):
            if i > count:
                return False
            count = max(count, i + nums[i])
        if count >= len(nums) - 1:
            return True



