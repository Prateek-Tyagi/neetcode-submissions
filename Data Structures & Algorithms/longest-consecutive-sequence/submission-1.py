class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # creat a set of this list
        numset = set(nums)
        # set the longest to zero
        longest = 0
        # we check for each numbers in set - list is in set now and sets are unordered
        for num in numset:
            # starting the sequence with the number that not has its previous number in this list
            if num-1 not in numset:
                current = num
                length = 1
                
                # check the next number if num+1 exists in sequence, if yes doing it again
                while current+1 in numset:
                    current +=1
                    length +=1
                
                longest = max(longest, length)
        
        return longest