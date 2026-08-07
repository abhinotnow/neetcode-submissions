import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #binary search on answer space
        max_rate = max(piles) + 1
        best_rate = None
        l = 1
        r = max_rate
        while l<=r:
            mid = (l+r)//2
            hrs = 0
            for pile in piles:
                if mid >= pile:
                    hrs+=1
                    continue
                else:
                    hrs += math.ceil(pile/mid)
            if hrs > h:
                l = mid+1
            elif hrs<=h:
                best_rate = mid
                r = mid-1
        return best_rate