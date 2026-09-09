class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n: int):
            count = 0

            while n:
                n &= (n - 1)
                count += 1
            return count

        res = []
        for i in range(0, n + 1):
            res.append(count(i))
        
        return res



        