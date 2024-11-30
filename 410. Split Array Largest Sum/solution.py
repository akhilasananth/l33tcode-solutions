from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasable(threshold: int) -> bool:
            count = 1
            total = 0

            for n in nums:
                total += n
                if total > threshold:
                    total = n
                    count += 1
                if count > k:
                    return False
            return True

        left, right = max(nums), sum(nums)

        while left < right:
            mid = left + (right - left) // 2

            if feasable(mid):
                right = mid
            else:
                left = mid + 1

        return left