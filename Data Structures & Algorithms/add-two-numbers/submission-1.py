# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        curr = l3
        carry = 0
        while(l1 and l2):
            if (l1.val + l2.val + carry >= 10):
                curr.next = ListNode(l1.val + l2.val + carry - 10)
                carry = 1
                curr = curr.next
            else:
                curr.next = ListNode(l1.val + l2.val + carry)
                carry = 0
                curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while(l1):
            if (l1.val + carry >= 10):
                curr.next = ListNode(l1.val + carry - 10)
                carry = 1
                curr = curr.next
            else:
                curr.next = ListNode(l1.val + carry)
                carry = 0
                curr = curr.next
            l1 = l1.next
        while(l2):
            if (l2.val + carry >= 10):
                curr.next = ListNode(l2.val + carry - 10)
                carry = 1
                curr = curr.next
            else:
                curr.next = ListNode(l2.val + carry)
                carry = 0
                curr = curr.next
            l2 = l2.next
        if carry == 1:
            curr.next = ListNode(1)
        return l3.next