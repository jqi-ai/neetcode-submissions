class TimeMap:

    def __init__(self):
        # atm: A Time Stamp
        self.atm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        item = (timestamp, value)
        if key in self.atm:
            self.atm[key].append(item)
        else:
            self.atm[key] = [item]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.atm:
            return ""
        arr = self.atm[key]
        i, j = 0, len(arr) - 1
        result = ""
        while i <= j:
            mid = (i + j) // 2
            (curr_t, curr_v) = arr[mid]
            if curr_t > timestamp:
                j = mid - 1
            else:
                result = curr_v
                i = mid + 1
        return result
