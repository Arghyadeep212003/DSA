class Solution(object):
    def totalFruit(self, fruits):
        low=0
        high=0
        f={}
        res=0     #or float(-inf) or -1

        for high in range(0,len(fruits)):
            num=fruits[high]
            f[num]=f.get(num,0)+1

            while len(f)>2:
                f[fruits[low]]-=1
                if f[fruits[low]]==0:
                    del f[fruits[low]]
                low+=1

            if len(f)<=2:
                length=high-low+1
                res=max(res,length)
        return res
        