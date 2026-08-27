class Solution:
    def countTriplets(self, sum, arr):
        #code here
        arr.sort()
        count=0

        for i in range(0,len(arr)-2):

            left=i+1
            right=len(arr)-1

            while(left<right):

                total=arr[i]+arr[left]+arr[right]

                if total>=sum:
                    right-=1

                else:
                    count+=right-left
                    left+=1

        return count