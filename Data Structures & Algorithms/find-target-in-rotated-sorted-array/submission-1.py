class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:  # Left half is sorted
                if nums[l] <= target < nums[m]:  # Is target in left sorted half?
                    r = m - 1
                else:
                    # search right
                    l = m + 1
            else:  # Right half is sorted
                if nums[m] < target <= nums[r]:  # Is target in right sorted half?
                    # search right
                    l = m + 1
                else:
                    # search left
                    r = m - 1
        return -1