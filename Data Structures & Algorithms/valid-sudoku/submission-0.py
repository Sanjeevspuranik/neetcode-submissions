class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # cell value
                val = board[r][c]

                # Filter empty values
                if val == ".":
                    continue
                
                # Check and Update
                if (
                    val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True
                

        