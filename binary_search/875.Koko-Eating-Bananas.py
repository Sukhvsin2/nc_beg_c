class Solution:
    def eatPile(self, piles: List[int], n: int) -> int:
        count:int = 0

        for i in piles:
            count += math.ceil(i/n)
        return count

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l<=r:
            mid = (l+r)/2

            if self.eatPile(piles, mid) <= h:
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
