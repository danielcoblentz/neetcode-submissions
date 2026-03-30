'''
input - string of chars
output - a single val representing the length of the longest substring w/o repeating hars from s
edge case(s): empty input --> 0?

time, space - O(n), O(n) wehre n is the lgnth of the input s

notes:

init a set, vars l,r and length which is the result

we use the poitners to check if the va lat the right poitner is is the set if it is we remove the val at left char

if its not we add it to the set and ocmpute the length because this is possiblyy better than the previously known one

we greedy choose the longest between the current window and running result

return length at the end rep the longest substring found
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0


        seen = set()
        l, r = 0, 0
        window = 0

        while r < len(s):
            # not seen yet
            if s[r] not in seen:
                seen.add(s[r])
                window = max(window, r - l + 1)
                r += 1

            # already in set
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
        return window
