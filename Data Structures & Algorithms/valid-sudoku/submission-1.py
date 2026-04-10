class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        memo = { }

        for i in range(len(board)):
            memo[f"row_{i}"] = []
            for j in range(len(board[i])):
                box = ""
                if f"col_{j}" not in memo:
                    memo[f"col_{j}"] = []

                # create a tuple to tell which box we're in
                box = (i//3, j//3)
                if box not in memo:
                    memo[box] = []
                
                cur = board[i][j]
                if cur != ".":
                    if cur in memo[f"col_{j}"] or cur in memo[f"row_{i}"] or cur in memo[box]:
                        return False
                    else:
                        memo[f"col_{j}"].append(board[i][j])
                        memo[f"row_{i}"].append(board[i][j])
                        memo[box].append(board[i][j])

        return True
