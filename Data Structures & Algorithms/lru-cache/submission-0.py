class LRUCache:

    def __init__(self, capacity: int):
        self.order = 0
        self.lru = {}
        self.size = 0
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        [value, _] = self.lru[key]
        self.lru[key] = [value, self.order]
        self.order += 1
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key] = [value, self.order]
            self.order += 1
        else:
            self.lru[key] = [value, self.order]
            self.order += 1
            self.size += 1
            if self.size > self.cap:
                self.size -= 1
                key_remove, key_order = None, self.order + 1
                for k, item in self.lru.items():
                    [val, order] = item
                    if order < key_order:
                        key_order = order
                        key_remove = k
                del self.lru[key_remove]
        return None
