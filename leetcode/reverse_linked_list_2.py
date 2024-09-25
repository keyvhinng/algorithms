from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left==right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy

        for i in range(left-1):
            prev = curr
            curr = curr.next

        for i in range(right-left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next

def printList(head: Optional[ListNode]) -> None:
    it = head
    count = 0
    while it and count<10:
        print(it.val)
        it = it.next
        count += 1
        
        
sol = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

ans = sol.reverseBetween(n1,2,4)
printList(ans)
