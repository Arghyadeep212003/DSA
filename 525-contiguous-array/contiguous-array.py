class Solution(object):
    def findMaxLength(self, nums):
        zero=0
        one=0
        f={}
        res=0

        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            
            diff=zero-one

            if diff==0:
                res=max(res,i+1)
                # continue
            
            if diff in f:
                length=i-f[diff]
                res=max(length,res)
            
            else:
                f[diff]=i
            
        return res
        