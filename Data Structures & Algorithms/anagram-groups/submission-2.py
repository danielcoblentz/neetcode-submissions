'''
edge case no input


init a defaultdict for grouping <tuple[ord]: [str1,...strn]>
iterate through the input and convert the strs[i] into the ord representatio. in an array
check if in dict if it is append the str (not encoded) if it is not we add it 

return the default dict.items()

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = defaultdict(list)

        for s in strs:
            # convert and make tuple
            tmp = [0] * 26
            for c in s:
              tmp[ord(c) - ord('a')] += 1
            count[tuple(tmp)].append(s)
        return list(count.values())
            

        