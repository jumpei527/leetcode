# n: number of elements in the linked list
# Time: O(n)
# Space: O(1)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            next_tmp = cur.next
            cur.next = prev
            prev = cur
            cur = next_tmp

        return prev
