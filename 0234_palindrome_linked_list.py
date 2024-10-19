# Time: O(n)
# Space: O(n)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_val = []
        while head:
            list_val.append(head.val)
            head = head.next
        left = 0
        right = len(list_val) - 1
        while left < right:
            if list_val[left] != list_val[right]:
                return False
            left += 1
            right -= 1
        return True
