class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq  = deque()
        for right in range(len(nums)):
            # remove the index that are out of the current window
            if dq and dq[0] <= right - k:
                dq.popleft()
            
            # remove the index from the right if right idex has value bigger then right
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()
            dq.append(right)

            if right >= k - 1:
                result.append(nums[dq[0]])
        
        return result