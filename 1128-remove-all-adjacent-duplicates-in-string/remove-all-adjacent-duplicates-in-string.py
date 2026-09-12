class Solution(object):
    def removeDuplicates(self, s):
        res=[]
        st=[]

        for i in range(len(s)):
            if len(st)==0:
                st.append(s[i])

            elif st[-1]==s[i]:
                st.pop()
            else:   
                st.append(s[i])
        
        while len(st)!=0:
            res.append(st[-1])
            st.pop()
        res.reverse()
        return "".join(res)
        