# n: number of nodes
# Time: O(n)
# Space: O(1)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        if not head:
            return

        node_length = 1
        cur = head
        while cur.next:
            node_length += 1
            cur = cur.next
        cur.next = head
        k %= node_length
        for _ in range(node_length - k):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        return new_head
