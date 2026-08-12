class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        n = len(nums)

        def count(remaining: int):
            if remaining == 0:
                return 1

            if remaining < 0:
                return 0

            cache_key = remaining
            if cache_key in cache:
                return cache[cache_key]

            result = sum(count(remaining - num) for num in nums)
            cache[cache_key] = result
            return result

        return count(target)
            