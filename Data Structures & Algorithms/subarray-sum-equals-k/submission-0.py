class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0

        hashmap = {}
        hashmap[0] = 1

        for num in nums:
            prefix += num

            if prefix - k in hashmap:
                count += hashmap[prefix - k]

            hashmap[prefix] = hashmap.get(prefix, 0) + 1

        return count
        