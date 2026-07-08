class Solution(object):
    def removeKdigits(self, num, k):
        st=[]
        for i in num:
            while st and st[-1]>i and k:
                st.pop()
                k-=1
            st.append(i)
        if k>0:
            st=st[:-k]
        ans="".join(st).lstrip("0")
        return ans if ans else "0"
       
        