class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        ans = 0
        l = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            window = (r - l) + 1
            maxF = max(count.values())
            while window - maxF > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
                window = (r - l) + 1
                maxF = max(count.values())
            ans = max(ans, window)
        return ans