class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sset = set(nums)
        res = 0
        for n in nums:
            if not (n-1 in sset):
                seq = 1
                while (n + seq) in sset:
                    seq += 1
                res = max(res, seq)
        return res