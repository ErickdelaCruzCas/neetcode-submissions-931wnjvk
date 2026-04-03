class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        res = float("inf")
        currSum = 0
        for R in range(len(nums)):
            currSum += nums[R]
            while L <= R and currSum >= target:
                res = min(res, R - L + 1)
                currSum -= nums[L]
                L += 1
            
        return 0 if res == float("inf") else res