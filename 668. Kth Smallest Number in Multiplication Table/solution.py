class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def condition(num: int) -> bool:
            num_k = sum(min(num // i, n) for i in range(1, m + 1))

            return num_k < k

        left, right = 1, m * n

        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                left = mid + 1
            else:
                right = mid

        return left
