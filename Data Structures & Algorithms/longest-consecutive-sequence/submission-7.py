class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longest = 0

        for n in num:
            if n - 1 not in num:
                leng = 1

                while n + leng in num:
                    leng += 1

                longest = max(longest, leng)

        return longest