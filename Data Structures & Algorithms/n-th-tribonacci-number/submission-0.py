class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}

        def evaluate(i: int):
            if i == 0: return 0

            if i == 1 or i == 2: return 1

            if i in cache:
                return cache[i]

            result = evaluate(i-1) + evaluate(i-2) + evaluate(i-3)
            cache[i] = result
            return result

        return evaluate(n)

        
        
        