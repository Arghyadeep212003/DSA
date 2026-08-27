class Solution(object):
    def sortedSquares(self, nums):
        left=0
        right=len(nums)-1

        result=[0]*len(nums)   #Create an empty result array of the same size as nums, filled with 0s, so we can replace those 0s with the sorted squares. The * operator repeats the list.

        id=len(nums)-1

        while left<=right:
            leftsq=nums[left]*nums[left]
            rightsq=nums[right]*nums[right]

            if leftsq>rightsq:
                result[id]=leftsq
                left+=1
            
            else:
                result[id]=rightsq
                right-=1

            id-=1

        return result
        