class Solution:
    def _rob(self, nums: list[int], index: int, memo: dict) -> int:
        key_ = index
        if key_ in memo:
            return memo[key_]
        
        if index >= len(nums):
            return 0
        
        memo[key_] = nums[index] + max(
            self._rob(nums, index + 2, memo),
            self._rob(nums, index + 3, memo)
        )
        return memo[key_]

    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        memo = {}

        return max(
            self._rob(nums[:-1], 0, {}),
            self._rob(nums, 1, memo),
            self._rob(nums, 2, memo),
        )