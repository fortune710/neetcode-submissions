class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        n = len(s)

        def findWord(index: int):
            if index == n:
                return True

            if index in cache:
                return cache[index]

            for word in wordDict:
                if s[index:].startswith(word):

                    if findWord(index + len(word)):
                        cache[index] = True
                        return True

            cache[index] = False
            return False

        return findWord(0)