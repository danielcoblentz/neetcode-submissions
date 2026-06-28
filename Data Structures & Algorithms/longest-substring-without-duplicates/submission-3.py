'''
if we add a char to the set we increment += 1
opposite case: if current char in set then we want to remove that cha increment l += 1 


'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        seen = set()
        ans = 0
        l = 0


        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            ans = max(ans, r - l + 1)
        return ans
