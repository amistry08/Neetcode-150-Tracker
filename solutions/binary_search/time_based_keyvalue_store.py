class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((timestamp, value))
        else:
            self.data[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
    
        res = ""
        val = self.data.get(key, [])
        l, r = 0, len(val)-1

        while l <= r:
            m = (l + r) // 2
            if val[m][0] <= timestamp:
                res = val[m][1]
                l = m + 1
            else:
                r = m - 1 
        
        return res


