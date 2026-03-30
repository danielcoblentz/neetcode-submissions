class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        algo: O(n), O(n) where  n  = len(s)
        two poitners + set approach
        zxyzxyz
        set = (zxy)
               l r

         l
        zxyzxyz
           r
        set (x,y)
        length = 3
        '''

        # edge case
        if len(s) == 0:
            return 0

        l, r = 0, 0
        max_length = 0
        char_set = set()

        while r != len(s):
            if s[r] not in char_set:
                #add + calc len
                char_set.add(s[r])
                current_length = len(char_set)
                max_length = max(max_length, current_length)
                r += 1
            else: # char must be present in set so remove s[l]
                char_set.remove(s[l])
                l += 1
        return max_length