# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        if current_node:
            next_node = head.next
            previous_node = None
            while next_node != None:
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
                next_node = next_node.next
            current_node.next = previous_node
        return current_node