"""

input: arrr of ints in inc order and a target value we need to check for
want: the 1-idx position of elements hwich sum to target

edge case(s): empty input or missing target or not found a valid combination what do we return??

time, space -
exp:
since it is is increasing order we cna use tow ptrs and position them at hte beginning and end of hte array
while l < r we get a current sum and chcek if it is greater than the target we decrement hte right pointer because we know the order is sorted
and that will decrment hte current sum and vice versa for hte left poitner once we find a valid comibnation we add list(l + 1, r + 1) for hte 1 based idx and reutn that

"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # edge case(s)

        # main
        l, r = 0, len(numbers) - 1

        while l < r:
            currS = numbers[l] + numbers[r]
            if currS == target:
                return [l + 1, r + 1]
            elif currS < target:
                l += 1
            else:
                r -= 1
