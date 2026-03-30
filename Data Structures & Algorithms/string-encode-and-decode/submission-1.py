'''
input: 1D list of strings
output: edcoded version of same 1D list of strings
edge case: empty input what do we return?

time, space - O(n), O(n) because we have the output array

notes:

encode func()
1) iteate through the input we need a way to seperate each word from the list individually
2) we can use a non-ascii delimiter followed by the number of chars
    2.1) Hello --> #5Hello#5World

decode func()
1) we need to use the info #5 to know when to start and stop reading characters from the input
2) after we read each encoded message we append it to the result list which we return at the end after processing everything

'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs is None:
            return [""]

        encoded = []
        for word in strs:
            encoded += str(len(word)) + '#' + word
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
                
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end
        return res
        
