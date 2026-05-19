import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points: return 0
        heap = []

        # compute dist & push to heap
        for x, y in points:
            dist = ((x - 0)**2 + (y - 0)**2)
            heapq.heappush(heap, (dist, x, y))
        
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res
