# n = len(nums)
from typing import List


class Solution:
    # Time: O(nlogn)
    # Space: O(1)
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product_of_three_largest = nums[-3] * nums[-2] * nums[-1]
        product_with_two_smallest = nums[0] * nums[1] * nums[-1]

        return max(product_of_three_largest, product_with_two_smallest)


class Solution2:
    # Time: O(n)
    # Space: O(1)
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = float("-inf")
        max2 = float("-inf")
        max3 = float("-inf")
        min1 = float("inf")
        min2 = float("inf")

        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, max1 * min1 * min2)
