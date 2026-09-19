class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        alphabetLimit = 26

        while columnNumber > 0:
            quotient = columnNumber // alphabetLimit
            remainder = columnNumber % alphabetLimit
            
            if remainder == 0:
                remainder = 26
                quotient = 0

            sheet = chr(65 + remainder - 1)
            result = sheet + result
            columnNumber = quotient

        return result