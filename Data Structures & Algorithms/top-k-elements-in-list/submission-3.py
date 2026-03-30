import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        algo 1) min-heap T: O(n log k), O(n + k)
        hash --> count freq of each num in nums:
        use a min heap to store tuple(freq, num)
                                        0,    1
        if len(heap) > k:
            heapq.heappop(heap)

        res = [] --> output
        for i in range(k):
            res.append(heap[1])
        return res

        algo 2) bucket sort, T: O(n), O(n)
        TODO
        '''

        count, res, heap = {}, [], []

        # pop hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)  
            # print(count) 

        for key, val in count.items():
            heapq.heappush(heap, (val, key))

        # correct size of heap
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


