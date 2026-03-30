class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(1, n + 1)}
        res = {i : float('inf') for i in range(1, n + 1)}
        res[k] = 0

        # populate
        for src, dst, time in times:
            adj[src].append([dst, time])
        min_heap = [[0, k]]

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            
            if w1 > res[n1]:
                continue

            for n2, w2 in adj[n1]:
                if res[n1] + w2 < res[n2]:
                    res[n2] = res[n1] + w2
                    heapq.heappush(min_heap, [res[n2], n2])

        ans = max(res.values())
        return ans if ans != float('inf') else -1