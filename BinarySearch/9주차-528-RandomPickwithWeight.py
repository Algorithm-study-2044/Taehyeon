import random

class Solution:

    def __init__(self, w: List[int]):
        self.aggre = [0 for _ in range(len(w))]
        self.total = sum(w)
        for _ in range(len(w)):
            w[_] = w[_]/self.total
        for _ in range(len(w)):
            if _ == 0:
                self.aggre[_] = w[_]
            else:
                self.aggre[_] = self.aggre[_ - 1] + w[_]

    def pickIndex(self) -> int:
        left = 0; right = len(self.aggre)- 1
        N = random.uniform(0, 1)

        while left < right:
            mid = left + (right - left)//2
            if self.aggre[mid] >= N:
                right = mid
            else:
                left = mid + 1

        return left
        
        return self.aggre[left]


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()