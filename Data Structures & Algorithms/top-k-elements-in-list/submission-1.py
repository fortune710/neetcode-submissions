from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        result = []

        for key, value in hashmap.items():
            heappush(result, (value, key))

            if len(result) > k:
                heappop(result)

        return [num for _, num in result]
