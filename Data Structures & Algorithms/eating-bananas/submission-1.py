import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        max_rate = max(piles)
        best_rate = math.inf
        r = max_rate
        while l<=r:
            mid = (l+r)//2
            hrs = 0
            for pile in piles:
                if mid>=pile:
                    hrs +=1
                else:
                    hrs += math.ceil(pile/mid)
            if hrs > h:
                l = mid+1
            else:
                best_rate = min(best_rate, mid)
                r = mid-1
        return best_rate