class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        n = len(nums)

        if n == 1:
            return nums[0]

        def travel(index: int, start: int, cache: dict):
            if index < start:
                return 0

            if index in cache:
                return cache[index]

            option_1 = travel(index - 2, start, cache) + nums[index]
            option_2 = travel(index - 1, start, cache)

            cache[index] = max(option_1, option_2)
            return cache[index]

        case_1 = travel(n - 2, 0, {})
        case_2 = travel(n - 1, 1, {})

        return max(case_1, case_2)