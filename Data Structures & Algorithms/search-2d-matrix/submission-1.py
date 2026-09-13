class Solution:
    def binarySearch(self, matrix, target, start, end, row):
        if end <= start:
            return False
        mid = (start + end) // 2
        if (matrix[row][mid] == target):
            return True
        elif (matrix[row][mid] > target):
            return self.binarySearch(matrix, target, start, mid, row)
        else:
            return self.binarySearch(matrix, target, mid + 1, end, row)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                break
        row = i

        return self.binarySearch(matrix, target, 0, len(matrix[0]), row)