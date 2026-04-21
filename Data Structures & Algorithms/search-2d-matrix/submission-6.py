class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        good_row = None

        while low <= high:
            mid = low + (high - low) // 2

            if target > matrix[mid][-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                good_row = matrix[mid]
                break

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
            