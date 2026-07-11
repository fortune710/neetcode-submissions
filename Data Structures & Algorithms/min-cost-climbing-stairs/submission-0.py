class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [0] * (n + 1)

        def travel(index: int):
            if index <= 1:
                return 0

            if cache[index] != 0:
                return cache[index]

            option_1 = travel(index - 1) + cost[index - 1]
            option_2 = travel(index - 2) + cost[index - 2]
            cache[index] = min(option_1, option_2)

            return cache[index]

        return travel(n)

            