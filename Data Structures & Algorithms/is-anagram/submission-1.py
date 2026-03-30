from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_1 = Counter(s)
        count_2 = Counter(t)
        if count_1 == count_2: 
            return True
        else: 
            return False