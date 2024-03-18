class Solution:
    memo = [0 for i in range(50)]
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if Solution.memo[n] != 0:
                return Solution.memo[n]
            else:
                Solution.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
                return Solution.memo[n]
        