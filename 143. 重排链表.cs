/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public void ReorderList(ListNode head) 
    {
        ListNode mid = FindMid(head);
        ListNode rp = ReverseList(mid);
        MergeList(head,rp);
    }

    public ListNode FindMid(ListNode head)
    {
        ListNode slow = head;
        ListNode fast = head.next;
        while(fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public ListNode ReverseList(ListNode head)
    {
        ListNode prev = null;
        ListNode current = head;

        while (current != null) {
            ListNode nextNode = current.next;
            current.next = prev;

            prev = current;
            current = nextNode;
        }
        return prev; // 返回反转后的头节点
    }

    public void MergeList(ListNode lp,ListNode rp)
    {
        while(lp != null && rp != null)
        {
            ListNode lpNext = lp.next;
            ListNode rpNext = rp.next;

            lp.next = rp;
            rp.next = lpNext;

            lp = lpNext;
            rp = rpNext;
        }
    }
}