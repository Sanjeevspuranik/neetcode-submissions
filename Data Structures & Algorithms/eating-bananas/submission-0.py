class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best_speed = right

        while left <= right:
            mid = left + (right -left) // 2

            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
            
            if total_hours <= h:
                best_speed = mid
                right = mid - 1
            
            else:
                left = mid + 1
        
        return best_speed
        