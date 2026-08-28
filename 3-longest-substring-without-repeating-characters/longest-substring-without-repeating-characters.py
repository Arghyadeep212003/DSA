class Solution(object):
    def lengthOfLongestSubstring(self, s):
        low=0
        high=0
        res=0
        freq={}

        for high in range(0,len(s)):
            ch=s[high]
            freq[ch]=freq.get(ch,0)+1

            k=high-low+1

            while len(freq)<k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
                k=high-low+1

            length=high-low+1
            res=max(length,res)

        return res

        