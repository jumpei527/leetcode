class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        value = ""

        left = -1
        right = len(values)
        while right - left > 1:
            mid = (left + right) // 2
            time_mid = values[mid][0]
            val_mid = values[mid][1]

            if time_mid <= timestamp:
                value = val_mid
                left = mid
            else:
                right = mid

        return value


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
