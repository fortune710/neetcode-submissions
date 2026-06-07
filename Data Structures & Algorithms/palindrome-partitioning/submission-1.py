class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(word: str):
            return word == word[::-1]

        def backtrack(currentIndex: int, palindromes: List[str]):
            if currentIndex == len(s):
                result.append(palindromes[:])
                return

            for i in range(currentIndex, len(s)):
                substring = s[currentIndex : i + 1]

                if is_palindrome(substring):
                    palindromes.append(substring)
                    backtrack(i + 1, palindromes)
                    palindromes.pop()

        backtrack(0, [])
        return result