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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy_node = ListNode(0)
        dummy_node.next = head

        odd_node = head
        even_node = head.next
        even_head = even_node

        while even_node and even_node.next:
            odd_node.next = odd_node.next.next
            even_node.next = even_node.next.next
            odd_node = odd_node.next
            even_node = even_node.next
        odd_node.next = even_head

        return dummy_node.next
