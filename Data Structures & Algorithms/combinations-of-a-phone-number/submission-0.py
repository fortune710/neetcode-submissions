class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if not digits:
            return []

        result = []

        def backtrack(index: int, word: str):
            if len(word) == len(digits):
                result.append(word)
                return

            characters = keys[digits[index]]
            for i in range(len(characters)):
                temp = word
                word += characters[i]
                backtrack(index + 1, word)
                
                word = temp

        backtrack(0, "")
        return result