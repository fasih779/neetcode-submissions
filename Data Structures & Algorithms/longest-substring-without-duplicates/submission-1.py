class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ha = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in ha:
                ha.remove(s[l])
                l += 1

            ha.add(s[r])
            res = max(res, r - l + 1)

        return res