class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # this gonna has pairs of (index, height)
        maxArea = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height: # if current bar is shorter then the bar in stack
                idx, h = stack.pop() # extract the pair - starting_index and height of the bar
                width = i - idx  # width distance from current index and the existing bar index
                maxArea = max(maxArea, h * width) # calculate the area of that bar
                start = idx # because the next shorter bar starts from the index of existing longer bar - shorter bar starting index is supported by higher bar
            stack.append((start, height)) # if current bar is not a wall, add it to stack

        for idx, height in stack:
            width = len(heights) - idx
            area = height * width
            maxArea = max(maxArea, area)

        return maxArea
                