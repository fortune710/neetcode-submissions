class Solution:
    def countSubstrings(self, s: str) -> int:
        count  = 0
        cache = {}
        n = len(s)

        def is_palindrome(i, j) -> bool:
            if i >= j:
                return True
            
            if (i, j) in cache:
                return cache[(i, j)]

            cache[(i, j)] = (s[i] == s[j]) and is_palindrome(i + 1, j - 1)
            return cache[(i, j)]

        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j):
                    count += 1

        return count