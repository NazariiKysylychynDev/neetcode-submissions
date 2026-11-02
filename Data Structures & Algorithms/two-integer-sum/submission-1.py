class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_ = i = 0

        for j in range(len(nums)):
            sum_ += nums[j]

            if sum_ == target:
                return [i, j]
            if sum_ >= target:
                sum_ -= nums[i]
                i += 1

        return [0, j]
        
        
