class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        result = dict.fromkeys(range(max(nums) + 1), True)
        for i in nums:
            if result[i] == False:
                return i
            result[i] = False
        return -1