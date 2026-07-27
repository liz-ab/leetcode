class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        map=Counter(magazine)
        for ch in ransomNote:
            if ch not in map or map[ch]==0:
                return False
            map[ch]-=1
        return True
        