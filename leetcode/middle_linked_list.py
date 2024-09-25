from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        count = 1
        while fast and fast.next:
            count = 0
            slow = slow.next
            fast = fast.next.next
        return slow
