# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        c=0
        while cur:
            c+=1
            cur=cur.next
        for i in range(c//2):
            head=head.next
        return head
            
        