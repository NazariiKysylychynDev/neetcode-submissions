class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid
            else:
                return mid 
        return -1