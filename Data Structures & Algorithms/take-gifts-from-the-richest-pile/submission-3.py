import math
import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            l = -heapq.heappop(heap)
            heapq.heappush(heap, -int(math.sqrt(l)))

        return -sum(heap)
