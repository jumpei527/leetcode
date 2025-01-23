# n: node_count
# Time: O(n)
# Space: O(n)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next
            else:
                prev = cur
            cur = cur.next

        return head
