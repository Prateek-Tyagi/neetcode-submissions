import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = 0
    
        while left <= right:
            mid = (left + right) // 2
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile/mid)
                
            
            if total_hours <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer


        
        