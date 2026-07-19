class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s)) <= 1:
            return len(s)
        l, r = 0, 1
        visited = set([s[l]])
        char_index = {s[l]: l}
        res = 1
        while l < r and r < len(s):
            candidate = s[r]
            if candidate in visited:
                while l < r:
                    removed = s[l]
                    if removed in char_index:
                        del char_index[removed]
                    visited.remove(removed)
                    l += 1
                    if removed == candidate:
                        break
            visited.add(candidate)
            char_index[candidate] = r
            res = max(res, r - l + 1)
            r += 1
        return res