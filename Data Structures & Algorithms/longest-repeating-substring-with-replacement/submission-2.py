class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        ha = {}

        for r in range(len(s)):
            ha[s[r]] = ha.get(s[r], 0) + 1

            if (r - l + 1) - max(ha.values()) <= k:
                res = max(res, r - l + 1)
            else:
                ha[s[l]] -= 1
                l += 1

        return res