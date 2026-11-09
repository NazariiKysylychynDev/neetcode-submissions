class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_ = 0

        lo, hi = 0, len(height) - 1

        while lo < hi:
            max_ = max(max_, (hi - lo) * min(height[hi], height[lo]))

            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return max_
