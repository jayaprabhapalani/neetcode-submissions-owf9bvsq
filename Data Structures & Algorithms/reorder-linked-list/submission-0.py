# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle
        s,f=head,head.next
        while f and f.next:
            s=s.next
            f=f.next.next

        #rev the second half
        
        cur=s.next
        s.next=None
        prev=None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp

        #merging them
        l,r=head,prev
        while r:
            temp1,temp2=l.next,r.next
            l.next=r
            r.next=temp1
            l=temp1
            r=temp2



        