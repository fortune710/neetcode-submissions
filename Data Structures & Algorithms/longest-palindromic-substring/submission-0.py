class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        cache = {}
        palindrome = ""

        def is_palindrome(i: int, j: int) -> bool:
            if len(s[i:j+1]) <= 1:
                return True

            if (i, j) in cache:
                return cache[(i, j)]
            
            result = (s[i] == s[j]) and is_palindrome(i + 1, j - 1)
            cache[(i, j)] = result
            return result

        for i in range(n):
            for j in range(i, n):
                if is_palindrome(i, j):
                    if not palindrome or j - i + 1 > len(palindrome):
                        palindrome = s[i: j+1]

        return palindrome
        

        