class Solution(object):
    def countStudents(self, st, sa):
        stack=[]
        c=0
        length=len(st)*len(sa)
        while(c!=length):
            if(len(st)==0):
                return 0
            if(st[0]==sa[0]):
                st.pop(0)
                sa.pop(0)
            else:
                c=c+1
                k=st.pop(0)
                st.append(k)
        return len(st)

        