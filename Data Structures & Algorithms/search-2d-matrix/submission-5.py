class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        good_row = None

        while low <= high:
            mid = low + (high - low) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target and mid + 1 <= len(matrix) - 1 and matrix[mid + 1][0] > target:
                good_row = matrix[mid]
                break
            elif matrix[mid][0] < target and mid + 1 > len(matrix) - 1:
                good_row = matrix[mid]
                break
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1

        if good_row == None:
            return False

        low = 0
        high = len(good_row) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if good_row[mid] == target:
                return True
            elif good_row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
            