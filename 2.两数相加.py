# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        up = 0
        res = ListNode()
        pre = res
        while l1 != None or l2 != None:
            res.next = ListNode()
            res = res.next
            if l1 != None:
                res.val += l1.val
                l1 = l1.next
            if l2 != None:
                res.val += l2.val
                l2 = l2.next
            res.val += up
            if res.val >= 10:
                res.val -= 10
                up = 1
            else:
                up = 0
        if up == 1:
            res.next = ListNode(1)

        return pre.next