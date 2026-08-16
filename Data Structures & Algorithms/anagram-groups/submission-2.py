class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = defaultdict(list)
        for string in strs:
            counter = Counter(string)
            key = frozenset(counter.items())
            storage[key].append(string)
        return [value for value in storage.values()]