class Solution:
    def maxArea(self, heights: List[int]) -> int:
    

        left = 0
        right = len(heights) - 1

        MaxArea = 0

        while left != right:
            # calculate the width of the container - distance between left and right bar
            width = right - left
            # calculate the height that we take so both the container holds the water  - need to take the minimum of both bar height
            container_wall = min(heights[left], heights[right])
            # calculate the Area of the container - width times lower height bar
            area = width * container_wall

            # record the max area 
            MaxArea = max(MaxArea, area)
            
            # adjust the pointers - Move right if current height is lower, move left if walls at right side are lower
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -=1
        return MaxArea

            

        