class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = dict()
        for string in strs:
            counter = Counter(string)
            key = frozenset(counter.items())
            if key in storage:
                storage[key].append(string)
            else:
                storage[key] = [string]
        return [value for value in storage.values()]