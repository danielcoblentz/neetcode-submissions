class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(idx, memo):
            if idx == len(s): return True
            if idx in memo: return memo[idx]

            for word in wordDict:
                if s[idx:idx + len(word)] == word:
                    if dfs(idx + len(word), memo):
                        memo[idx] = True
                        return True
            memo[idx] = False
            return False


        return dfs(0, {})
        