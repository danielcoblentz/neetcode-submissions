import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        res = []
        for n in nums:
            count[n]=count.get(n, 0) + 1
        
        for n, c in count.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
        