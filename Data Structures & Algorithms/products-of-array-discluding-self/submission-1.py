class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = []
        suffix = []

        
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                product *= nums[i - 1]
                prefix.append(product)

       
        j = len(nums) - 1
        d = 1

        while j >= 0:
            if j == len(nums) - 1:
                suffix.append(1)
            else:
                d *= nums[j + 1]
                suffix.append(d)
            j -= 1

        
        suffix.reverse()
        print(suffix)
        print(prefix)
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i])

        return ans           
                


                      