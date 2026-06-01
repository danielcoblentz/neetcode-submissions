class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       count = {}

       for i in range(len(nums)):
        diff = target - nums[i]
        if nums[i] in count:
            return [count[nums[i]], i]
        else:
            count[diff] = i