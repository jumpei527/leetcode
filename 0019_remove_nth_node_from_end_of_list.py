# n: node_count
# Time: O(n)
# Space: O(1)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        cur = head
        right = head
        for _ in range(n):
            right = right.next

        prev = None
        while right:
            prev = cur
            cur = cur.next
            right = right.next

        if not prev:
            return head.next

        prev.next = cur.next
        return head
