class Solution(object):
    def sqSum(self,n):
        sum=0
        while n>0:
            d=n%10
            n=n//10
            sum+=d*d
        return sum

    def isHappy(self, n):
        slow=n
        fast=n

        while fast!=1:
            slow=self.sqSum(slow)
            fast=self.sqSum(fast)
            fast=self.sqSum(fast)

            if slow==fast and slow!=1:
                return False

        return True
        