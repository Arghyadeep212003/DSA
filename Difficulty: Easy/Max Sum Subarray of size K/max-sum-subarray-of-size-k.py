class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        low=0
        high=k # or can write k
        sum=0


        for i in range(low,high):
            sum+=arr[i]

        res=sum  # or can write 0

        while high<len(arr):

            sum=sum-arr[low]+arr[high]

            res=max(res,sum)
            low+=1
            high+=1

        return res