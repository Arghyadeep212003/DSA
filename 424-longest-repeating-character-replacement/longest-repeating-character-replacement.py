class Solution(object):
    def characterReplacement(self, s, k):
        low=0
        high=0
        f={}
        maxFreq=0
        res=0

        for high in range (0,len(s)):
            ch=s[high]
            f[ch]=f.get(ch,0)+1

            maxFreq=max(maxFreq,f[ch])
            length=high-low+1
            diff=length-maxFreq

            while diff>k:
                f[s[low]]-=1
                low+=1

                length=high-low+1
                diff=length-maxFreq

            length=high-low+1
            res=max(res,length)

        return res

        