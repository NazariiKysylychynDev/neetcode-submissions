class Solution:
    def climbStairs(self, n):
        return self._climbStairs(n, {})

    def _climbStairs(self, n: int, memo: dict) -> int:
        key_ = n
        if key_ in memo:
            return memo[key_]

        if n <= 1:
            return 1
        
        memo[key_] = self._climbStairs(n-1, memo) + self._climbStairs(n-2, memo)
        return memo[key_]