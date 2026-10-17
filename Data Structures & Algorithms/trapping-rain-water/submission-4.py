class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = 0
        rightMax = 0
        left = 0
        right = len(height) - 1
        water = 0
        while left <= right:
            if leftMax <= rightMax:
                    leftMax = max(leftMax, height[left])
                    water += leftMax - height[left]
                    left += 1
            else:
                rightMax = max(rightMax,height[right])
                water += rightMax - height[right]
                right -= 1
        return water

        
        