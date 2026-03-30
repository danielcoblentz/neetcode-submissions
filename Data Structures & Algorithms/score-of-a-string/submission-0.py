class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            char1, char2 = ord(s[i]), ord(s[i + 1])
            score += abs(char1 - char2)
        return score