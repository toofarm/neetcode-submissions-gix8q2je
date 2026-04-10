class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        memo = { }

        for i in range(len(board)):
            memo[f"row_{i}"] = []
            for j in range(len(board[i])):
                box = ""
                if f"col_{j}" not in memo:
                    memo[f"col_{j}"] = []
                # use these vars to find out which box we're in
                row = "1" if i < 3 else "2" if i < 6 else '3'
                col = "1" if j < 3 else "2" if j < 6 else '3'
                box = f"box_{row}_{col}"
                if box not in memo:
                    memo[box] = []
                
                if board[i][j] != ".":
                    memo[f"col_{j}"].append(board[i][j])
                    memo[f"row_{i}"].append(board[i][j])
                    memo[box].append(board[i][j])

        for val in memo.values():
            dupes = [i for i in set(val) if val.count(i) > 1]
            if len(dupes) > 0:
                return False

        return True
