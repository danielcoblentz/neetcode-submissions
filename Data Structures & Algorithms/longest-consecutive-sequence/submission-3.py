class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest_streak = 0

        for n in seen:
            if n - 1 not in seen:  # only start at the beginning of a sequence
                curr = n
                streak = 1
                while curr + 1 in seen:
                    curr += 1
                    streak += 1
                longest_streak = max(longest_streak, streak)

        return longest_streak
