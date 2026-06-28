class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        sorted_only = sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = sorted_only[:k]

        ans = []

        for num, freq in result:
            ans.append(num)

        return ans