class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ha = {}

        for i in nums:
            ha[i] = ha.get(i, 0) + 1

        v = ha.items()
        s = sorted(v, key=lambda v: v[1], reverse=True)

        l = []

        for n, v in s:
            if k > 0:
                l.append(n)
                k -= 1
            else:
                break

        return l