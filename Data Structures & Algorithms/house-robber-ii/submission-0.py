class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
    
        def helper(arr: List[int]):
            rob1, rob2 = 0, 0
            for n in arr:
                # looking backwards only
                tmp = max(rob1 + n, rob2)
                # transition
                rob1 = rob2
                rob2 = tmp
            return rob2

        # exclude first hous1
        print(nums[1:n+1], nums[:n])
        res1 = helper(nums[1:n+1])



        # exclude second house
        res2 = helper(nums[:n-1])

        # return ans
        return max(res1, res2)


