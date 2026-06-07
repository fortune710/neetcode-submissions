class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        i = 0
        j = i + 1

        while i < len(heights) - 1:
            if j >= len(heights):
                j = 0
                i += 1
                continue
            
            diff = abs(j - i)
            container_height = min(heights[i], heights[j])
            if container_height * diff > max_water:
                max_water = container_height * diff
            
            j += 1

        return max_water