class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(word: str):
            return word and word == word[::-1]

        def backtrack(currentIndex: int, partition: List[str]):
            ## Base Case
            if currentIndex == len(s):
                result.append(partition[:])
                return

            for i in range(currentIndex, len(s)):
                substring = s[currentIndex : i + 1]

                if is_palindrome(substring):
                    partition.append(substring)

                    backtrack(i + 1, partition)

                    partition.pop()

        backtrack(0, [])
        return result