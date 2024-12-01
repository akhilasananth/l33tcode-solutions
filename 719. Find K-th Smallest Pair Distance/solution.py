class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def condition(distance: int) -> bool:
            count, i, j = 0, 0, 0

            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += j - i - 1
                i += 1

            return count >= k

        left, right = 0, nums[n - 1] - nums[0]

        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left


