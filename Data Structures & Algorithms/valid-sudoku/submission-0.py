class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue 

                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True

# rows[r] gives a set of digits seen in row r

# cols[c] gives a set of digits seen in column c

# squares[(r // 3, c // 3)] gives a set of digits seen in that 3x3 square

# Because they are defaultdict(set), the first time you access a given key, you automatically get an empty set for that key.