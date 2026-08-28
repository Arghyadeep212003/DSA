class Solution(object):
    def longestOnes(self, nums, k):
        low=0
        high=0
        zeroCount=0
        res=0

        for high in range (0,len(nums)):
            if nums[high]==0:
                zeroCount+=1

            while(zeroCount>k):
                if nums[low]==0:
                    zeroCount-=1
                
                low+=1

            length=high-low+1
            res=max(res,length)
        
        return res
        