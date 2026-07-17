class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        res=[]
        def backtrack(combinations,nextDigit):
            if not nextDigit:
                res.append(combinations)
                return
            for letter in phone[nextDigit[0]]:
                backtrack(combinations+letter,nextDigit[1:])
        backtrack("",digits)
        return res

