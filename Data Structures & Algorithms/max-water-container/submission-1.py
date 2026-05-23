class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ans = 0

        while l < r:
            current_area = min(heights[l], heights[r]) * (r - l)
            ans = max(ans, current_area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return ans