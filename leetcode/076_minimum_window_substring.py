class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        map = [0] * 128
        for c in t:
            map[ord(c)] += 1

        l = 0
        count = 0
        start = 0
        min_len = float("inf")

        for r in range(len(s)):
            curChar = s[r]
            if map[ord(curChar)] > 0:
                count += 1
            map[ord(curChar)] -= 1

            while count == len(t):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l
                
                char_l = s[l]
                map[ord(char_l)] += 1
                if map[ord(char_l)] > 0:
                    count -= 1
                l += 1
        return "" if min_len == float("inf") else s[start : start + min_len]       