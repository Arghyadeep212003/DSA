class Solution(object):
    def maxProduct(self, nums):
        maxEnd=nums[0]
        minEnd=nums[0]
        res=nums[0]

        for i in range(1,len(nums)):
            v1=nums[i]
            v2=maxEnd*nums[i]
            v3=minEnd*nums[i]

            maxEnd=max(v1,max(v2,v3))
            minEnd=min(v1,min(v2,v3))

            res=max(res,max(maxEnd,minEnd))

        return res
        