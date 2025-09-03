class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        product = 0
        for num in nums:
            product = product ^ num

        bit = product & (-product)
        res = [0, 0]
        for num in nums:
            if num & bit == 0:
                res[0] = res[0] ^ num
            else:
                res[1] = res[1] ^ num

        return res