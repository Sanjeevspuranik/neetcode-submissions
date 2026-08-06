class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for word in strs:
            signature = "".join(sorted(word))
            seen[signature].append(word)
        
        return list(seen.values())