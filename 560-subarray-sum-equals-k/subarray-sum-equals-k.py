class Solution(object):
    def subarraySum(self, nums, k):
        current_sum=0
        prefix={}
        prefix={0:1}
        res=0

        for i in range(len(nums)):
            current_sum+=nums[i]
            need=current_sum-k

            if need in prefix:
                res+=prefix[need]
            
            prefix[current_sum]=prefix.get(current_sum,0)+1

        return res
        