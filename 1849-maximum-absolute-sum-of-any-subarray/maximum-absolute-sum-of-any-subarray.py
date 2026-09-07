class Solution(object):
    def maxAbsoluteSum(self, nums):
        maxSum=nums[0]
        minSum=nums[0]
        res=abs(nums[0])

        for i in range(1,len(nums)):
            v1=nums[i]
            v2=maxSum+nums[i]
            v3=minSum+nums[i]

            maxSum=max(v1,max(v2,v3))
            minSum=min(v1,min(v2,v3))

            res=max(abs(res),max(abs(maxSum),abs(minSum)))

        return res
        