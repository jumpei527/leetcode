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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        dummy = ListNode(0)
        dummy.next = head
        slow_node = dummy
        fast_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        slow_node.next = slow_node.next.next

        return dummy.next
