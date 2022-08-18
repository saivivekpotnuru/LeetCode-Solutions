# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Naive approach
        #count the nodes and find the len-n th node
        
        #two pointer approach using fast and slow 
        #intally move fast upto n nodes and then move slow and fast simultaneously the res will be at slow
        
        fast,slow=head,head
        for i in range(n):
            fast=fast.next
        if not fast:
            return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head
            