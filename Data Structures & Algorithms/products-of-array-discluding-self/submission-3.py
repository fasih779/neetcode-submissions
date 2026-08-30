class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        suff = []
        pre = []
        prod = 1
        i = 0

        while i < len(nums):

            pre.append(prod)
            prod *= nums[i]

            i += 1

        j = len(nums) - 1
        po = 1

        while j >= 0:

            suff.append(po)
            po *= nums[j]

            j -= 1

        suff.reverse()

        res = []
        i = 0

        while i < len(nums):

            res.append(pre[i] * suff[i])

            i += 1

        return res