from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count, wind = Counter(t), {}

        have, need = 0, len(count)
        p = 0
        resleg = float("infinity")
        res = [0, 0]

        for c in range(len(s)):
            l = s[c]
            wind[l] = wind.get(l, 0) + 1

            if l in count and wind[l] == count[l]:
                have += 1

            while have == need:
                if (c - p + 1) < resleg:
                    res = [p, c + 1]
                    resleg = c - p + 1

                wind[s[p]] -= 1

                if s[p] in count and wind[s[p]] < count[s[p]]:
                    have -= 1

                p += 1

        return s[res[0]:res[1]]