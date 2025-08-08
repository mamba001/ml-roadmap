class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robber(nums):
            pre1, pre2 = 0, 0
            for num in nums:
                cur = max(pre1 + num, pre2)
                pre1 = pre2
                pre2 = cur
            return pre2
        return max(robber(nums[:-1]), robber(nums[1:]))    