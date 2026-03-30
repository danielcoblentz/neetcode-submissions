class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        for idx in range(len(nums)):
            if idx != nums[idx]:
                return idx
        
        return len(nums)