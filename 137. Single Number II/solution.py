class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once, thrice = 0, 0
        for n in nums:
            once = (once ^ n) & ~thrice
            thrice = (thrice ^ n) & ~once

        return once