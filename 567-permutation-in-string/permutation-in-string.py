class Solution(object):
    def checkInclusion(self, s1, s2):
        k=len(s1)
        l=0
        h=0
        need={}
        wind={}

        if len(s1)>len(s2):
            return False

        for ch in s1:
            need[ch]=need.get(ch,0)+1

        for h in range(0,len(s2)):
            wind[s2[h]]=wind.get(s2[h],0)+1
            length=h-l+1

            while length>k:
                wind[s2[l]]-=1
                if wind[s2[l]]==0:
                    del wind[s2[l]]
                l+=1
                length=h-l+1
            
            if need==wind:
                return True
            
        return False