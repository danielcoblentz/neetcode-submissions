class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''

        for str in s:
            if str.isalnum():
                new_str += str.lower()
        return new_str == new_str[::-1]
