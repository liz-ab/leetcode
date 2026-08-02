class Solution(object):
    def uniqueOccurrences(self, arr):
        n=Counter(arr)
        s=set()
        for i in n.values():
            if i in s:
                return False
            s.add(i)
        return True