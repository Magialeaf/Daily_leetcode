# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dic = {}
        for i,link in enumerate(lists):
            while link:
                if link.val in dic:
                    dic[link.val].append(i)
                else:
                    dic[link.val] = [i]
                link = link.next

        keys = sorted(dic.keys())
        temp = ListNode(0)
        res = temp

        for key in keys:
            for val in dic[key]:
                temp.next = lists[val]
                temp = temp.next
                lists[val] = lists[val].next

        return res.next