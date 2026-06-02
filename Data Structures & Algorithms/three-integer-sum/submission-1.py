class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for m in range(len(nums)):
            if m > 0 and nums[m] == nums[m-1]:
                continue
            l, r = m + 1, len(nums) - 1
            while l < r:
                tmp = nums[l] + nums[m] + nums[r]
                if tmp == 0:
                    res.append([nums[m], nums[l], nums[r]]) 
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                elif tmp < 0:
                    l += 1
                else:
                    r -= 1
        return res