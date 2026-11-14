class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}!{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        cursor = 0
        while cursor < len(s):
            jump = ""
            while s[cursor] != "!":
                jump += s[cursor]
                cursor += 1
            cursor += 1
            jump = int(jump)
            res.append(s[cursor:cursor+jump])
            cursor += jump
        return res
