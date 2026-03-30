class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def solve(i, subset):
            if i  == len(nums):
                res.append(subset[::])
                return
            
            # we include nums[i]
            subset.append(nums[i])
            solve(i + 1, subset)
            subset.pop()

            # do not include nums[i], is it in range? [1, 2, 2, 2, 3]
            while i + 1 < len(nums) and nums[i] == nums[i  + 1]:
                i += 1
            solve(i + 1, subset)


            return res
        return solve(0, [])