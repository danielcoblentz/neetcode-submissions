class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        ans = nums[0]
        curMax, curMin = 1, 1

        for i in range(len(nums)):
            tmp = curMax
            curMax = max(nums[i], nums[i] * curMax, nums[i] * curMin)
            curMin = min(nums[i], nums[i] * tmp, nums[i] * curMin)
            ans = max(ans, curMax)

        return ans