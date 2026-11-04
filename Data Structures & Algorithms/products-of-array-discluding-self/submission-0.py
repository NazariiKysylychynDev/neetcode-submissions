from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        if zero_count == 1:
            product_without_zero = reduce(lambda x, y: x * y, (n for n in nums if n != 0))
            return [product_without_zero if n == 0 else 0 for n in nums]

        full_product = reduce(lambda x, y: x * y, nums)

        res = []
        for n in nums:
            res.append(full_product // n)

        return res