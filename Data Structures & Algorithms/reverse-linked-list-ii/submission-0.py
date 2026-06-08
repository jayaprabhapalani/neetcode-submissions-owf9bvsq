# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head

        # dummy node to handle left=1
        dummy=ListNode()
        dummy.next=head
        prev_left=dummy

        #find the first segment
        for _ in range(left-1):
            prev_left=prev_left.next

        cur=prev_left.next

        #reverse the sublist in place
        prev=None
        for _ in range(right-left+1):
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur=next_node

        # reconnect the reverse segment
        prev_left.next.next=cur #connect the end of the reversed segment
        prev_left.next=prev #   Connect the left segment to the new head of the reversed segment

        return dummy.next     





        