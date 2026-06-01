'''
input: lst of ints 
want: a boolean representing if there a re duplicates present in the input -- T if yes False otherwis

edge case: anything other thans ints? T/F or empty arr?


exp: 
all all items to the set since sets must contian unique vlaues we cna check the lengthis if htye are equal then there are no duplicates
so return false if the count is different then we return true indicating here must be a dup somewhere (does not matter where)
time, space - (n), O(n) - for adding items to thte set then holding them




'''



class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        print(seen)
        if len(nums) == len(seen):
            return False
        else:
            return True
