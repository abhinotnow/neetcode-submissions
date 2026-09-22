from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap[key]
        
        l = 0
        r = len(values)-1
        best = -1

        while l<=r:
            mid = (l+r)//2

            if values[mid][0] <= timestamp:
                best = mid
                l = mid+1
            else:
                r = mid-1
        
        if best == -1:
            return ""
            
        return values[best][1]