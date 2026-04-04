class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        ns, np = len(s), len(p)
        if ns < np:
            return False
        

        p_count = Counter(p)
        s_count = Counter()

        for i in range(ns):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            if p_count == s_count:
                return True

        return False