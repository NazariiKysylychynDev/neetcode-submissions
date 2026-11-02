class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_ = i = 0

        for j in range(len(nums)):
            sum_ += nums[j]

            while sum_ > target:
                sum_ -= nums[i]
                i += 1

            if sum_ == target and j != i:
                return [i, j]

        return [0, j]
        
        
