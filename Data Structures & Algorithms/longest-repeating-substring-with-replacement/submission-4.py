class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0
        l= 0 

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(count.values())

            if (r - l + 1) - maxF <= k:
                ans = max(ans, (r - l + 1))
            else:
        # k too small shrink window
                count[s[l]] -= 1
                if count[s[l]] == 0:
                        del count[s[l]]
                l += 1
            
        return ans