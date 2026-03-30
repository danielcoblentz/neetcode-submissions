class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # Odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                res += 1
                r += 1
                l -= 1
            
            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                res += 1
                r += 1
                l -= 1
                
        return res