class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map_ = dict()  # target - num : index 

        for i, num in enumerate(numbers):
            reduce = target - num

            if reduce in map_:
                return [map_[reduce] + 1, i + 1]
            map_[num] = i
        return []