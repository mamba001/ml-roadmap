class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        pre1 = 1
        pre2 = 2
        for i in range(3, n + 1):
            cur = pre1 + pre2
            pre1 = pre2
            pre2 = cur
        return pre2
        