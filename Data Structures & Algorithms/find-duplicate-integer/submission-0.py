class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set()
        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
        return 0
        