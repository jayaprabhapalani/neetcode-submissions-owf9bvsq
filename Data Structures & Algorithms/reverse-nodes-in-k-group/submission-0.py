# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        group_prev=dummy

        while True:
            #find the kth node of the current group
            kth=self.getKthNode(group_prev,k)
            if not kth:
                break

            next_group=kth.next

            #reversse the k-group
            curr=group_prev.next
            prev_node=next_group

            while curr !=next_group:
                next_node=curr.next
                curr.next=prev_node
                prev_node=curr
                curr=next_node

            #connect the group_prev to the new head
            temp=group_prev.next
            group_prev.next=kth
            group_prev=temp

        return dummy.next

    def getKthNode(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr            