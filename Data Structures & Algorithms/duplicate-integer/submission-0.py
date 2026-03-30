class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valid_set = set()
        for n in nums:
            if n not in valid_set:
                valid_set.add(n)
    
        if len(valid_set) == len(nums):
            return False
        else: return True