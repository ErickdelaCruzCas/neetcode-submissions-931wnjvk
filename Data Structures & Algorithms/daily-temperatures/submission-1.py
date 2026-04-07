class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and temps[i] > temps[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)

        return res