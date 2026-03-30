'''
input - string of uppercase chars

output - the longest possible substring if we did k replacements and its valid

edge case(s) - empty input, we know we are guarentted a uppercase string of chars, any nums or other ascii chars?

time, space - 

notes - 
1) we can check for edge cases
2) init a hashmap and a poitner with a var for maintaining the longest knwon length in our problem (return it at the end)
3) iterate over the string add aech char to the hmap so we know its frequecny each time we check the max occuring char and if it is 
<= to the k val we can compute the length by applying (r - l + 1 + maxfreqchar)
maintin hte current length and max freq char if that difference is less than or equal to k we cna do replacements
4) greedy choose the previous known max and comapre to this new val bc it can be better than the prev one

5) return the window



'''



class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        count = {}
        longest_seq = 0
        l = 0 

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            
            max_freq = max(count.values())

            #less than k
            window_len = r - l + 1
            if window_len - max_freq <= k:
                longest_seq = max(longest_seq, window_len)
            else:
                if count[s[l]] >= 1:
                    count[s[l]] -= 1
                else:
                    del count[s[l]]
                l += 1

        return longest_seq


        