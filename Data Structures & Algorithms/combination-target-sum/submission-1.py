class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def backtrack(start, path, cur_sum):
            # base cases --> success
            if cur_sum == target:
                res.append(path[::])
                return 
            if cur_sum > target: #(optimization)
                return 


            # otherwise
            for j in range(start, len(nums)):
                path.append(nums[j])
                backtrack(j, path, cur_sum + nums[j])
                path.pop()

        backtrack(0, [], 0)
        return res