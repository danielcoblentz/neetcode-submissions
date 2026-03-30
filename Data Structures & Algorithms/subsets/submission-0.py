class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [],[]

        def backtrack(index, path):
            if index >= len(nums):
                res.append(path[:])
                return

            # choose the num
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()


            # dont choose
            backtrack(index + 1, path)
        backtrack(0, [])

        return res