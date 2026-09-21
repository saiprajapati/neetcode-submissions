# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        back = ListNode(None, head)
        front = head
        h = back
        for _ in range(1,n):
            front = front.next
        while front.next:
            back = back.next
            front = front.next
        back.next = back.next.next

        return h.next