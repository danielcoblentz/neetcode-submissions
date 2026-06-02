'''
input
want:

edge case(s)

time, space

exp:
we use the bitwise not operator to check eac hvlue and the all function which return true if there are all truthy vlaues within it
'''













class Solution:
    def isPalindrome(self, s: str) -> bool:
       s = [c.lower() for c in s if c.isalnum()]
       return all(s[i] == s[~i] for i in range(len(s) // 2))