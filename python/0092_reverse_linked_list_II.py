# n: link_count
# Time: O(n)
# Space: O(1)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
            self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head
        startLeft = dummy

        for _ in range(left - 1):
            startLeft = cur
            cur = cur.next

        prev = None
        for _ in range(right - left + 1):
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

        startLeft.next.next = cur
        startLeft.next = prev

        return dummy.next
