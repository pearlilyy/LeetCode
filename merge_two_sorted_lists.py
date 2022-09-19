# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoLists(self, list1, list2):

        if list1 == [] or list2 == []:
            return list1 + list2

        # smaller list would be the head
        if list1.val < list2.val:
            temp = head = ListNode(list1.val)
            list1 = list1.next
        else:
            temp = head = ListNode(list2.val)
            list2 = list2.next

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            temp = temp.next

        while list1 is not None:
            temp.next = ListNode(list1.val)
            list1 = list1.next
            temp = temp.next
        while list2 is not None:
            temp.next = ListNode(list2.val)
            list2 = list2.next
            temp = temp.next

        return head
