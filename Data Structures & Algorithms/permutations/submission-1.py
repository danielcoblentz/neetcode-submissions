class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        def solve(i, nums):
            if i == len(nums):
                return [[]]
            res = []
            perms = solve(i + 1, nums)

            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            return res
        return solve(0, nums)