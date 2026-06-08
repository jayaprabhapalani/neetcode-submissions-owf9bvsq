# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle
        if not head or not head.next:
            return True
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        slow.next=None
        #reverse the second half
        prev=None
        while second:
            next_node=second.next
            second.next=prev
            prev=second
            second=next_node

        #compare 
        first=head
        #prev==second
        while first and prev:
            if first.val != prev.val:
                return False
            first=first.next
            prev=prev.next    
        return True                
        