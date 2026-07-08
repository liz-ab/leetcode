class Solution(object):
    def countStudents(self, st, sa):
        count=[st.count(0),st.count(1)]
        for i in sa:
            if(count[i]==0):
                break
            count[i]-=1
        return sum(count)

        