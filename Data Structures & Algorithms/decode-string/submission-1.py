class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                sbs = ""
                while stack[-1] != "[":
                    sbs = stack.pop() + sbs
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * sbs)
        
        return "".join(stack)