
'''
input: arr of strings
want: nested list of all strings that can be anagrams


edge case(s): empty input, all alphanum chars? upper, lowercase chars do we need to handle??

exp: 
we can init a defaultdict(list) then iterate over the input string we need to use the ord function
to compute the ascii value if each char and use a freq arr that will count hte freqw of each char of hte input
we will use this as hte key to our dict and we can do O(1) lookups for check ing of hte freq match (use tuples as hte key bc mutable objs cannot be keys in maps!)

return count.itemsvalues() in al ist format
act = [1,0,1,...1,...]

- dict = {[0,1,0,1...]: [ans]}


time, space - O(n), O(1) bc we only have 26 chars to compute each key is finite unless we allow more chars






'''







class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for char in s:
                arr[ord(char) - ord('a')] += 1
            myDict[tuple(arr)].append(s)
   
        return list(myDict.values())