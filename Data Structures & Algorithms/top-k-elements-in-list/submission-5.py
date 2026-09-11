import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        lst = set()
        for num in nums:
            d[num] = d.get(num, 0) + 1
        lst = sorted(d, key = d.get, reverse=True)[:k]
        return lst