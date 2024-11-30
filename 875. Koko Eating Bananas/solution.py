import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasable(k: int) -> bool:
            hours = sum(math.ceil(pile/k) for pile in piles)
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left)//2

            if feasable(mid):
                right = mid
            else:
                left = mid + 1
        return left