class Solution(object):
    def findDuplicate(self, nums):
        f={}

        for fast in range(0,len(nums)):
            ch=nums[fast]
            f[ch]=f.get(ch,0)+1

            if f[ch]>1:
                return ch