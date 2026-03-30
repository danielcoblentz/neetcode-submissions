class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        given our input array --> [2,20,4,10,3,4,5]
        we can check if hte current n-1 is present in hte set if it is then we can keep increasing our 
        streak and take hte max of our longest and streak then return longest
        '''
        if not nums:
            return 0
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # only try to build sequence from start of the sequence
            if num - 1 not in num_set:
                current = num
                streak = 1

                while current + 1 in num_set:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest
