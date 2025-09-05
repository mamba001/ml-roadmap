class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        level = []
        def dfs(index):
            if index == len(nums):
                res.append(level[:])
                return

            level.append(nums[index])
            dfs(index + 1)
            level.pop()

            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1
            dfs(index + 1)
            
        dfs(0)
        return res