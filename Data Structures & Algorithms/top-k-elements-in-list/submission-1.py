class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        topKList = frequency.most_common(k)

        return [tuple[0] for tuple in topKList]
        
        
        