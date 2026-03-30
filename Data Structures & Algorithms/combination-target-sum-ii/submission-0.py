class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # same a comb sum b w dps
        res, path = [], []
        candidates.sort()

        def backtrack(index, path):
            #base case
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return

    
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res