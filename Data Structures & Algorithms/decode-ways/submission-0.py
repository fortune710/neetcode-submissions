import string

class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        n = len(s)
        cache = {}

        def decode(index: int):
            if index >= n:
                return 1

            if index in cache:
                return cache[index]

            if s[index] == "0":
                return 0

            case_1 = decode(index + 1)
            case_2 = decode(index + 2) if (n - index + 1) >= 2 and 10 <= int(s[index:index+2]) <= 26 else 0

            total_ways = case_2 + case_1
            cache[index] = total_ways
            return total_ways

        return decode(0)