class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        text = s

        while l < r:
            text[l], text[r] = text[r], text[l]
            l += 1
            r -= 1