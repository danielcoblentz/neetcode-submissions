

'''

ans = [(30, 1)]
s = [(38)]
is next greater than curernt? if yes then we append hte resut and forget aobut it
if we see a new higher tmp than the current (what will curernt be?) we add the pair (tmp, position) to a stack





'''












class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        s = [] # [tmp, idx]

        for i, v in enumerate(temperatures):
            while s and v > s[-1][0]:
                prev_v, prev_i = s.pop()
                ans[prev_i] = i - prev_i
            s.append((v, i))
        return ans
