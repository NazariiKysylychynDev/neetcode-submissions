class Solution:
    def _minCostClimbingStairs(self, cost: list[int], index, memo) -> int:
        key_ = index

        if key_ in memo:
            return memo[key_]

        if index >= len(cost):
            return 0

        memo[key_] = cost[index] + min(self._minCostClimbingStairs(cost, index + 1, memo),
        self._minCostClimbingStairs(cost, index + 2, memo)
        )
        return memo[key_]

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}
        return min(self._minCostClimbingStairs(cost, 0, memo),
        self._minCostClimbingStairs(cost, 1, memo)
        )
