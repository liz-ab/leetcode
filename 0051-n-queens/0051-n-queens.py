class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.']*n for _ in range(n)]
        cols=set()
        pos_d=set()
        neg_d=set()
        def backtrack(r):
            if (r==n):
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r+c) in pos_d or (r-c) in neg_d:
                    continue
                board[r][c]='Q'
                cols.add(c)
                pos_d.add(r+c)
                neg_d.add(r-c)
                backtrack(r+1)
                board[r][c]='.'
                cols.remove(c)
                pos_d.remove(r+c)
                neg_d.remove(r-c)
        backtrack(0)
        return res
        