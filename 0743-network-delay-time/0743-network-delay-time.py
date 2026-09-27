class Solution(object):
    def networkDelayTime(self, times, n, k):
        edges=collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append([v,w])
        minH=[[0,k]]
        t=0
        visit=set()
        while minH:
            w1,v1=heapq.heappop(minH)
            if v1 in visit:
                continue
            visit.add(v1)
            t=max(t,w1)
            for v2,w2 in edges[v1]:
                if v2 not in visit:
                    heapq.heappush(minH,[w1+w2,v2])
        return t if len(visit)==n else -1
        