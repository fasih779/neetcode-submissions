class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i, j = 0, len(heights) - 1
        best = 0

        while i < j:
            distance = j - i
            shorter = min(heights[i], heights[j])
            area = shorter * distance
            best = max(best, area)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return best