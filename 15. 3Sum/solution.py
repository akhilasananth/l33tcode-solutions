class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        triplets = []

        for i, i_n in enumerate(nums):
            # we don't want to use the same value twice
            if i > 0 and i_n == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr_sum = i_n + nums[j] + nums[k]

                if curr_sum > target:
                    k -= 1
                elif curr_sum < target:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1

                    # we don't want to use the same value twice
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return triplets