# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, list1, list2):
        if not list1:
            return list2

        if not list2:
            return list1      

        list3 = ListNode(0)
        temp = list3

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next

        while list1:
            temp.next = list1
            list1 = list1.next
            temp = temp.next

        while list2:
            temp.next = list2
            list2 = list2.next
            temp = temp.next

        return list3.next
    
    def layers(self, lst):
        l = []
        i = 0

        while i < len(lst) - 1:
            l.append(self.merge(lst[i], lst[i + 1]))
            i += 2

        if len(lst) % 2 != 0:
            l.append(lst[-1])

        return l

    def mergeKLists(self, lists):
        if not lists:
            return None

        cond = True
        somelist = lists

        while cond:
            somelist = self.layers(somelist)

            if len(somelist) <= 1:
                cond = False

        return somelist[0]