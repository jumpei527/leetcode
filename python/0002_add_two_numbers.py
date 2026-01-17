# n = len(l1)
# m = len(l2)
# Time: O(max(n, m))
# Space: O(max(n, m))
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ans_start = ans
        carrynum = 0
        while l1 or l2 or carrynum:
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0

            tmp = l1_num + l2_num + carrynum
            value = tmp % 10
            carrynum = tmp // 10
            ans.next = ListNode(value)
            ans = ans.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans_start.next
