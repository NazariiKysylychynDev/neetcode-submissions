
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:  # O(3n + k) -> O(n)
        map_ = {}

        for i in nums: # O(n)
            map_[i] = map_.get(i, 0) + 1

        items = [(j, i) for i, j in map_.items()]  # O(n)
        heapq.heapify_max(items)  # O(n)
        # return [items[1] for i in range(k)]]  # O(k)

        return [heapq.heappop_max(items)[1] for _ in range(k)]