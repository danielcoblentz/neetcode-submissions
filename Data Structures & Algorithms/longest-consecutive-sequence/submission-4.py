class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1

        seen = set(nums)
        for num in seen:
            if num - 1 not in seen: # start of seq found
                tmp = 1
                while num + 1 in seen:
                    tmp += 1
                    num += 1
                ans = max(ans, tmp)
        return ans