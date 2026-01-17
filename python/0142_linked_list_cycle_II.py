# n: number of elements in the linked list
# Time: O(n)
# Space: O(n)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()

        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next

        return None
