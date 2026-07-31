class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def climb(index: int):
            if index == 0:
                return 1
                
            if index < 0:
                return 0
                
            if index in cache:
                return cache[index]

            option_1 = climb(index - 1)
            option_2 = climb(index - 2)
            cache[index] = option_1 + option_2
            return cache[index]

        return climb(n)


