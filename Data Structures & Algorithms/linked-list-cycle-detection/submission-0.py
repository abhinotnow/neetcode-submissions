# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        current_node = head
        if current_node:
            while current_node:
                if current_node in seen:
                    return True
                else:
                    seen.append(current_node)
                current_node = current_node.next
        return False