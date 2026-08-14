class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        cache = {}
        n = len(stoneValue)

        def play(index: int):
            if index == n:
                return 0

            if index in cache:
                return cache[index]

            elements_left = (n - 1) - index
            option_1 = stoneValue[index] - play(index + 1)
            option_2 = (stoneValue[index] + stoneValue[index+1]) - play(index + 2) if elements_left >= 1 else float('-inf')
            option_3 = (stoneValue[index] + stoneValue[index+1] + stoneValue[index+2]) - play(index + 3) if elements_left >= 2 else float('-inf')
            result = max(option_1, option_2, option_3)
            print(option_1, option_2, option_3)
            cache[index] = result
            return result

        res = play(0)
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"