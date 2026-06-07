# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Dummy=ListNode()
        Dummy.next=head
        cur=Dummy
        s=cur
        f=cur
        for _ in range(n):
            f=f.next

        while f and f.next:
            s=s.next
            f=f.next

        s.next=s.next.next 

        return Dummy.next       
        