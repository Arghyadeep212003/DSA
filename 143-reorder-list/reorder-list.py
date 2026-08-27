# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow=head
        fast=head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        slow.next=None
        temp=None

        while second!=None:
            nextNode=second.next
            second.next=temp
            temp=second
            second=nextNode

        l=head
        r=temp

        while r!=None:
            t1=l.next
            t2=r.next

            l.next=r
            r.next=t1

            l=t1
            r=t2
        