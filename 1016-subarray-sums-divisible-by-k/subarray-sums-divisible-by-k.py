class Solution:
    def subarraysDivByK(self, nums, k):
        total = 0
        f = {0: 1}
        res = 0

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k

            if rem < 0:
                rem += k

            if rem in f:
                res += f[rem]

            f[rem] = f.get(rem, 0) + 1

        return res