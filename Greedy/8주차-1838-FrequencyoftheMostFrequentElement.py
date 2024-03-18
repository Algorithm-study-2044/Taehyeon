class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums); k = k
        mpf = 1
        sigma = 0
        left = 0
        for ii, i in enumerate(nums):
            sigma += i
            while 1:
                if i*(ii-left+1) - sigma <= k:
                    break
                sigma -= nums[left]
                left += 1

            if mpf < ii - left + 1:
                mpf = ii - left + 1
        return mpf
