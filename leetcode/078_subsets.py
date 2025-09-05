class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        level = []
        def dfs(index):
            if index == len(nums):
                res.append(level[:])
                return
            
            dfs(index + 1)

            level.append(nums[index])
            dfs(index + 1)
            level.pop()
        dfs(0)
        return res