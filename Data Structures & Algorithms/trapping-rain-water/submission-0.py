class Solution:
    def trap(self, height: List[int]) -> int:
        l, trapped = 0,0
        r = len(height) - 1
        lMax, rMax = 0,0

        while l < r:
            cur_l = height[l]
            cur_r = height[r]

            lMax = max(cur_l, lMax)
            rMax = max(cur_r, rMax)

            if lMax < rMax:
                trapped += lMax - cur_l
                l += 1
            else:
                trapped += rMax - cur_r
                r -= 1
        return trapped