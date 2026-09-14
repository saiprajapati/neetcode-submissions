class Solution:
    def binarySearch(self, matrix, target, start, end, row):
        if start >= end:
            return False
        mid = (start + end) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] > target:
            return self.binarySearch(matrix, target, start, mid, row)
        else:
            return self.binarySearch(matrix, target, mid + 1, end, row)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix)

        while start < end:
            mid = (start + end) // 2

            if matrix[mid][-1] >= target:
                end = mid
            else:
                start = mid + 1
        row = start
        if row == len(matrix):
            return False
        return self.binarySearch(
            matrix, target, 0, len(matrix[0]), row
        )