class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result, start, end = 0, 0, 0
        ht = Counter()
        while start <= end and end < len(s):
            ht[s[end]] += 1
            [(_, star_count)] = ht.most_common(1)
            diff = ht.total() - star_count
            if (diff > k):
                while start <= end and diff > k:
                    ht[s[start]] -= 1
                    [(_, curr_count)] = ht.most_common(1)
                    diff = ht.total() - curr_count
                    start += 1
            curr = s[start:end+1]
            result = max(result, len(curr))
            end += 1
        return result