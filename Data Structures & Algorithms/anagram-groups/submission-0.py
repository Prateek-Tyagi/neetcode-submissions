class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for w in strs:
            key = "".join(sorted(w))
            groups[key].append(w)

        return list(groups.values())