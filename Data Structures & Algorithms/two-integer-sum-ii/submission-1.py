class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map_ = dict()  # target - num : index 

        for i, num in enumerate(numbers):
            reduce = target - num

            if reduce in map_ and reduce != num:
                break
            map_[num] = i
        return [map_[reduce] + 1, i + 1]
