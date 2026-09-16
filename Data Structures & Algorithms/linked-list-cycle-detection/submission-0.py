# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t = set()
        temp = head
        t.add(head)
        while temp:
            if temp.next in t:
                return True
            t.add(temp.next)
            temp = temp.next
        return False