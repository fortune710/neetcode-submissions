class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        def partition(index: int, remaining: int):
            if remaining == 0:
                return True

            if index == n and remaining != 0:
                return False

            cache_key = (index, remaining)
            if cache_key in cache:
                return cache[cache_key]

            option_1 = partition(index + 1, remaining)
            option_2 = partition(index + 1, remaining - nums[index])

            cache[cache_key] = option_1 or option_2
            return cache[cache_key]
        
        return partition(0, target)

        

        