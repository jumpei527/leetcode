# n = len(nums)
from typing import List


class Solution:
    # Time: O(nlogn)
    # Space: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    # Time: O(n)
    # Space: O(1)
    def majorityElement2(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

    # Time: O(n)
    # Space: O(n)
    def majorityElement3(self, nums: List[int]) -> int:
        num_length = len(nums)
        num_dict = {}

        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        for num, count in num_dict.items():
            if count > num_length // 2:
                return num
