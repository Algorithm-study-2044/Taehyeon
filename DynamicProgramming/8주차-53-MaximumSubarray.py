class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        sig = 0
        ans = nums[0]
        for right in range(len(nums)):
            sig += nums[right]
            if nums[right] > sig:
                left = right
                sig = nums[right]
            ans = max(ans, sig)
        return ans