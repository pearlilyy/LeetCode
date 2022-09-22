# 206.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if head is None:
            return head
        else:
            prev = head
            while prev.next:
                n = prev.next
                prev.next = n.next
                n.next = head
                head = n
            return head


# head = [1, 2, 3, 4, 5]
# Output = [5,4,3,2,1]
