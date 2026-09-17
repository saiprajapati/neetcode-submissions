class Solution:
    def binarySearch(self, nums, target, start, end):
        if start >= end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearch(nums, target, start, mid)
        else:
            return self.binarySearch(nums, target, mid + 1, end)

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums))