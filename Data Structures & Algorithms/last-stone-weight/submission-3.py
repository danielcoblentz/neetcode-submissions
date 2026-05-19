class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, s * -1)
      
        while len(heap) > 1:
            x, y = heapq.heappop(heap) * -1, heapq.heappop(heap) * -1
            if x != y:
                heapq.heappush(heap, -1 * abs(y - x))
        return -1 * heap[0] if heap else 0