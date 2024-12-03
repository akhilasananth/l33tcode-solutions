def perfect_square_condition(k: int, num: int) -> bool:
    return pow(k, 2) >= num


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left < right:
            mid = left + (right - left) // 2
            if perfect_square_condition(mid, num):
                right = mid
            else:
                left = mid + 1

        if pow(left, 2) != num:
            return False
        return True
