class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        q=deque()
        l=len(arr)
        q.append(start)
        while q:
            i=q.popleft()
            if arr[i]<0:
                continue
            if arr[i]==0:
                return True
            if arr[i]+i<l:
                q.append(arr[i]+i)
            if i-arr[i]>=0:
                q.append(i-arr[i])
            arr[i]=-arr[i]
        return False