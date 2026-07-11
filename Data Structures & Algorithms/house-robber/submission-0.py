class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        n = len(nums)

        def travel(index: int):
            if index < 0:
                return 0

            if index in cache:
                return cache[index]

            option_1 = travel(index - 2) + nums[index]
            option_2 = travel(index - 1)

            cache[index] = max(option_1, option_2)
            return cache[index]

        return travel(n - 1)