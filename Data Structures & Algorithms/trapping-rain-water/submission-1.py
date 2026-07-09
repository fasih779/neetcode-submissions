class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0

        for i in range(n):
            left_max = max(height[0:i+1])   # tallest from start up to i
            right_max = max(height[i:n])    # tallest from i to end
            water = min(left_max, right_max) - height[i]
            total += water

        return total