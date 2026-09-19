class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        topKList = frequency.most_common(k)

        return [tup[0] for tup in topKList]
        
        
        