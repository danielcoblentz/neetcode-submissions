from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        algo 1) T:O(m * nlog n) , S: O(m * n)
        hash[sorted_version_str: [str]]

        algo 2) T: O(m * n), S: O(m * n)
        [0] * 26
        [0,0,0,0,0,0,0,0,0] --> [2,0,1,...,1] : str associated w this key

        loop over [val for val in hash.values()]
        '''

        d_list = defaultdict(list) 

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            d_list[tuple(count)].append(s)
        return list(d_list.values())

