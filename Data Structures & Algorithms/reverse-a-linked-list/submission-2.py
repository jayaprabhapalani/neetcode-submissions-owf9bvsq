# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        curr=dummy
        prev=ListNode(None)
        while curr:
            next_node=curr.next
            prev.next=curr
            curr=next_node
            prev=prev.next
        return dummy.next




