class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        if len(nums) == 2: return max(nums)

        for n in nums:
            # rob1 = house we cannot take from at current because its adjacent
            # rob2 = house we can take from but need a way to incrment to account for all homes prev to it
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2