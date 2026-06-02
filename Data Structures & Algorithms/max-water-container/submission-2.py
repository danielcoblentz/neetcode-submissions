'''
input: an arr 'heights' that at each position is hte heights of a bar
want: the maximum amt of water (an int representation) we can hold within this array
edge case(s): no valid ans, missing heights array


time, space - O(n), O(1) - iterating through arr and using two ptrs

exp:
we init l, r --> pointers we use to traverse each position within hte array starting at 0 and len(input) - 1
next we use 'ans' to store our result of hte max water we can hold within the given input


check each bar heights only move the poitner that has a smaller bar heights and compute a tmp sum which we will
take hte maximum of that and the overall sum then return it at the end











'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights) - 1

        while l < r:
            tmp = min(heights[l], heights[r]) * (r - l)
            ans = max(tmp, ans)
            if heights[l] < heights[r]: l += 1
            elif heights[r] < heights[l]: r -= 1
            else:
                l += 1
                r -= 1
        return ans