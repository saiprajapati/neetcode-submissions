class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = 1
        suffix = 1
        n = len(nums) - 1
        for i in range(len(nums)):
            ans[i] *= prefix
            ans[n-i] *= suffix
            prefix *= nums[i]
            suffix *= nums[n-i]     
        return ans