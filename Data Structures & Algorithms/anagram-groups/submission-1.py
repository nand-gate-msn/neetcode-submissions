class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) # when lookup key that doesnt yet exist, creates that for you w a default value
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1 # calculates index based on ascii code - ord(ch) converts it to ascii
            anagram_map[tuple(count)].append(s) # use tuple() cuz dict cannot use list as key
        return list(anagram_map.values())