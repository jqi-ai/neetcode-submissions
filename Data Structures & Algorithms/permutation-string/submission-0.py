class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        i, j = 0, len(s1) - 1
        c2 = Counter(s2[i:j+1])
        while True:
            if c1 == c2:
                return True
            c2[s2[i]] -= 1
            i += 1
            j += 1
            if j >= len(s2):
                break
            c2[s2[j]] += 1
        return False