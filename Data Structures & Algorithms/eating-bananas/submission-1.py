class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        rate = high

        while low <= high:
            mid = low + (high - low) // 2
            total = 0

            for p in piles:
                total += math.ceil(p / mid)

            if total <= h:
                rate = min(mid, rate)
                high = mid - 1
            else:
                low = mid + 1

        return rate