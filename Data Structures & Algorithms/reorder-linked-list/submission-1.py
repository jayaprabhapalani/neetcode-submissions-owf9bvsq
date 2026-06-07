# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        
        #reverse the second half
        second=slow.next
        #setting  the first half end as none
        slow.next=None
        prev=None
        while second:
            next_node=second.next
            second.next=prev
            prev=second
            second=next_node

        #merge
        first=head
        while first and prev:
            tmp1,tmp2=first.next,prev.next
            first.next=prev
            prev.next=tmp1
            first=tmp1
            prev=tmp2
      


        