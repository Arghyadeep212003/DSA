class Solution(object):
    def findAnagrams(self, s, p):
        k=len(p)
        l=0
        h=0
        need={}
        wind={}
        ans=[]

        if len(p)>len(s):
            return []

        for ch in p:
            need[ch]=need.get(ch,0)+1

        for h in range(0,len(s)):
            wind[s[h]]=wind.get(s[h],0)+1
            length=h-l+1

            while length>k:
                wind[s[l]]-=1
                if wind[s[l]]==0:
                    del wind[s[l]]
                l+=1
                length=h-l+1
            
            if need==wind:
                ans.append(l)
            
        return ans

        