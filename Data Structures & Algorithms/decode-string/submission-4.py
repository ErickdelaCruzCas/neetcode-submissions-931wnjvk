class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        curr = ""
        k = 0
        for c in s:
            if c.isdigit():
                k = (k * 10) + int(c)
            elif c == "[":
                count = count_stack.append(k)
                stack = string_stack.append(curr)
                curr = ""
                k = 0
            elif c == "]":
                temp = curr
                count = count_stack.pop()
                curr = string_stack.pop()
                curr += count * temp        
            else:
                curr += c
        return curr