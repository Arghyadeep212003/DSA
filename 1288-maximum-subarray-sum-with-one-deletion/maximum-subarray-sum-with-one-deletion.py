class Solution(object):
    def maximumSum(self, arr):
        nodel=arr[0]
        onedel=0
        res=arr[0]

        for i in range(1,len(arr)):
            prev_nodel=nodel
            prev_onedel=onedel

            nodel=max(prev_nodel+arr[i],arr[i])
            # if prev_onedel==float(-inf):
            #     v=arr[i]
            # else:
            #     v=prev_onedel+arr[i]

            onedel=max(prev_onedel+arr[i],prev_nodel)

            res=max(res, max(nodel,onedel))
        return res
        