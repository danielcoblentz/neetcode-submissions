from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        # Always binary-search the *shorter* array
        if len(a) > len(b):
            a, b = b, a

        total = len(a) + len(b)
        half = total // 2

        l, r = 0, len(a)
        while l <= r:
            i = (l + r) // 2          # take i elements from a (left side size in a)
            j = half - i              # take j elements from b (left side size in b)

            aLeft  = a[i-1] if i > 0 else float("-inf")
            aRight = a[i]   if i < len(a) else float("inf")
            bLeft  = b[j-1] if j > 0 else float("-inf")
            bRight = b[j]   if j < len(b) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:  # odd
                    return min(aRight, bRight)
                # even
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2.0
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1
