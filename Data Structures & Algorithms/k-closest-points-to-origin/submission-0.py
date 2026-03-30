class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []
        for i in range(k):
            x, y = points[i]
            dist = x*x + y*y
            heapq.heappush(maxHeap, (-dist, x, y))
            
# loop through remaining points then compare them to top val
        for i in range(k, len(points)):
            x, y = points[i]
            dist = x*x + y*y
            if -dist > maxHeap[0][0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (-dist, x, y))

        # pop elemnts and return
        while maxHeap:
            _, x, y = heapq.heappop(maxHeap)
            res.append([x,y])

        return res
        



