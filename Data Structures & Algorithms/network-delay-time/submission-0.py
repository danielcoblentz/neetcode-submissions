'''
directed shorest path we know its a graph problem
and there are weigths on eac hedge this is likly dijkstras
we can keep track of a global min

use a heap and Bfs to explore the graph
but how do we know when we have all nodes visited and what do we reutrn? maybe the final node we isit we return that weight


time: O(E logE), where E is the number of edges.
'''





class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(1, n + 1)}

        for src, dst, wei in times:
            adj[src].append([dst, wei])

        shortest = {}
        minHeap = [[0, k]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        
        if len(shortest) != n:
            return -1
        return max(shortest.values())