class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, j = 1, max(piles)
        result = j
        while i <= j:
            curr = (i + j) // 2
            h_curr = self.calcHours(piles, curr)
            if h_curr > h:
                i = curr + 1
            else:
                result = min(result, curr)
                j = curr - 1
        return result
    def calcHours(self, piles, rate):
        result = 0
        for pile in piles:
            result += math.ceil(float(pile) / rate)
        return result