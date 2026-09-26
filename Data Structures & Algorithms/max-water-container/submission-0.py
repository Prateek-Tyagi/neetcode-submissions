class Solution:
    def maxArea(self, heights: List[int]) -> int:
    

        left = 0
        right = len(heights) - 1

        MaxArea = 0

        while left != right:
            Min = min(heights[left], heights[right])
            w   = right - left
            MaxArea = max(MaxArea, Min * w)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -=1
        return MaxArea

            

        