class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        n = len(costs) // 2
        res = 0
        for i in range(n):
            res += costs[i][0]
        for i in range(n, 2 * n):
            res += costs[i][1]
        return res