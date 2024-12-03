def sqrt_condition(k: int, x: int) -> bool:
    return pow(k, 2) <= x


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1

        while left < right:
            mid = left + (right - left) // 2
            if sqrt_condition(mid, x):
                left = mid + 1
            else:
                right = mid

        return left - 1
