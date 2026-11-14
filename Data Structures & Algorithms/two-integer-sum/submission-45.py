class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = {}
        for i,n in enumerate(nums):
            curr = target - n
            if curr in val_index:
                return [val_index[curr],i]
            val_index[n] = i
        return []
                