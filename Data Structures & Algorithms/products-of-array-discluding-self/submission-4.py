class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suff = []
        i, j = 0, len(nums) - 1
        res = []
        p = 1
        pr = 1

        while i < len(nums):
            if i == 0:
                pre.append(p)
            else:
                p *= nums[i - 1]
                pre.append(p)
            i += 1

        while j >= 0:
            if j == len(nums) - 1:
                suff.append(pr)
            else:
                pr *= nums[j + 1]
                suff.append(pr)
            j -= 1

        suff.reverse()

        for p, v in zip(pre, suff):
            res.append(p * v)

        return res