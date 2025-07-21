class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for w in strs:
            key = "".join(sorted(w))
            anagram_groups[key].append(w)

        return list(anagram_groups.values())