from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        pre1 = nums[0]
        pre2 = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            cur = max(pre2, pre1 + nums[i])
            pre1 = pre2
            pre2 = cur
        
        return pre2

        