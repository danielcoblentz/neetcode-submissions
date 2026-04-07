class Solution:
    def canJump(self, nums: List[int]) -> bool:


        # start from the end increment hte need every time we move to the next nums[i] position
        need = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= need:
                need = i
        return need == 0