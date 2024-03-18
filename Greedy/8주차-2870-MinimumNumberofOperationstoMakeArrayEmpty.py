class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 0
        counts = []
        attemps = 0
        for i in range(len(nums)):
            if i == 0: 
                count = 1
                continue

            if nums[i] == nums[i-1]:
                count += 1
            else:
                counts.append(count)
                count = 1

            if i == len(nums)-1:
                counts.append(count)
        for k in counts:
            if k == 1:
                return -1
            else:
                if k % 3 == 0:
                    attemps += k//3
                elif k % 3 == 1:
                    attemps += (k-4)//3 + 2
                else:
                    attemps += (k-2)//3 + 1
        return attemps