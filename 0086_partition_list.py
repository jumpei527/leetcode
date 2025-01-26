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
    def partition(
        self, head: Optional[ListNode], x: int
    ) -> Optional[ListNode]:
        small_dummy = ListNode()
        big_dummy = ListNode()
        small_tail = small_dummy
        big_tail = big_dummy

        cur = head
        while cur:
            if cur.val < x:
                small_tail.next = cur
                small_tail = small_tail.next
            else:
                big_tail.next = cur
                big_tail = big_tail.next
            cur = cur.next

        small_tail.next = big_dummy.next
        big_tail.next = None

        return small_dummy.next
