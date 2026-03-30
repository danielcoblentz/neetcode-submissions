class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R, maxArea = 0, len(heights) - 1, 0

        while L < R:
            #compute area
            curArea = (R - L) * min(heights[L], heights[R])
            maxArea = max(maxArea,curArea)
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return maxArea
        