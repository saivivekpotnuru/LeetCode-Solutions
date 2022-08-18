# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1,d2=headA,headB
        c1,c2=0,0
        while d1:
            c1+=1
            d1=d1.next
        while d2:
            c2+=1
            d2=d2.next
        d1,d2=headA,headB
        if c1>c2:
            temp=c1-c2
            while temp:
                d1=d1.next
                temp-=1
        else:
            temp=c2-c1
            while temp:
                d2=d2.next
                temp-=1
        while d1!=d2:
            d1=d1.next
            d2=d2.next
        return d1
                