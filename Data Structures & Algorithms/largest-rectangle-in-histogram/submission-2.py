class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                width = i - idx
                maxArea = max(maxArea, width * h)
                start = idx
            stack.append((start, height))

        
        for idx, height in stack:
            width = len(heights) - idx
            maxArea = max(maxArea, height * width)
        
        return maxArea