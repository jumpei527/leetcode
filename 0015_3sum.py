# n = len(nums)
# Time: O(n^2)
# Space: O(1)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]

                if cur_sum > 0:
                    k -= 1
                elif cur_sum < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return ans
