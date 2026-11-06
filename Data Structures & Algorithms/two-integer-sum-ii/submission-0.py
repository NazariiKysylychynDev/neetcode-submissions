class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map_ = set()  # target - num : index 

        for i, num in enumerate(numbers):
            reduce = target - num

            if reduce in map_ and reduce != num:
                break
            map_.add(num)
        return [reduce, num]
