from typing import List


def insert_condition(nums: List[int], k: int, target: int) -> bool:
    return nums[k] >= target


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if insert_condition(nums, mid, target):
                right = mid
            else:
                left = mid + 1

        return left
