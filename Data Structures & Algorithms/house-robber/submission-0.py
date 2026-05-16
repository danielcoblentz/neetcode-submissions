'''
input - arr of nums (ints)
output - maxiumm money we can steal from the homes in nums arr
edge case(s) - empty input, do we only have ints or can it be other data types??

time, space

notes:
want: maximum money from the arrwy without robbing neiboring homes
choices: we can take or skip 

considerations: we cannot have 2 neighbors at idx 0 or len(nums) - 1 can only have one if multiple elements are in the array

sample solution:

[1,1,3,3]

maxP = 0

if less than 2 elements: return max(nums)




'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 0: return 0
        if n <= 2: return max(nums)


        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2