class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers is None: return []
        n = len(numbers)
        l, r = 0, n -1

        while l < r:
            localCount = numbers[l] +  numbers[r]
            
            if localCount < target: 
                l +=1
            elif localCount > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []