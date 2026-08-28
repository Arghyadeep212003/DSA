class Solution(object):
    def minSubArrayLen(self, target, nums):
        low=0
        high=0

        result=float('inf')
        sum=0

        while high<len(nums):
            sum+=nums[high]
            
            while sum>=target:
                length=high-low+1
                result=min(result,length)

                sum-=nums[low]
                low+=1
        
            high+=1

        if result==float('inf'):
            return 0
        
        return result
        