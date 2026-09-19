class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arraySum = sum(nums)
        n = len(nums)
        sumIndex = n*(n+1)//2

        return sumIndex - arraySum
        