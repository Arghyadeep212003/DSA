# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow=head
        fast=head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        temp=None

        while slow!=None:
            nextNode=slow.next
            slow.next=temp
            temp=slow
            slow=nextNode

        l=head
        r=temp

        while r!=None:
            if l.val != r.val:
                return False

            l=l.next
            r=r.next
            
        return True
            