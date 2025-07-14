class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(nums, index, sum, temp):
            if sum == target:
                res.append(temp.copy())
                return
            
            if sum > target:
                return


            for i in range(index, len(nums)):
                temp.append(nums[i])
                dfs(nums, i, sum + nums[i], temp)
                temp.pop()

        
        dfs(candidates, 0, 0, [])
        return res