class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        maximum_count = 0
        for i in hs:
            if i - 1 in hs:
                continue
            count = 1
            req = i + 1
            while req in hs:
                count += 1
                req += 1
            maximum_count = max(maximum_count, count)
        return maximum_count