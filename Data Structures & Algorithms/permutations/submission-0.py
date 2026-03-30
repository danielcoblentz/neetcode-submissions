class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def backtrack(path):
            # base case
            if len(path) == len(nums):
                res.append(path[:])
                return
            if len(path) > len(nums):
                return

            # recursive case
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(path)
                path.pop()


        backtrack([])
        return res