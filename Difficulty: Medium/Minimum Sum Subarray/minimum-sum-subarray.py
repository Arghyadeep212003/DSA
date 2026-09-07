class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        best=arr[0]
        ans=arr[0]

        for i in range (1,len(arr)):
            v1=best+arr[i]
            v2=arr[i]

            best=min(v1,v2)
            ans=min(best,ans)

        return ans