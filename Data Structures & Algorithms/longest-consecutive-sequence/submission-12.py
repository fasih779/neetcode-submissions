class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        lon=0
        for n in num:
            if (n-1) not in num:
                le=1
                while(n+le in num):
                    le+=1
                lon=max(lon,le)
        return lon  