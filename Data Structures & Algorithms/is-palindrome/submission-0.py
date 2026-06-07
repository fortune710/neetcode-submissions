class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = s.lower().strip(' ')
        new_string = "".join(filter(str.isalnum, new_string))

        i = 0
        j = len(new_string) - 1

        try:
            while i < j:
                if new_string[i] == new_string[j]:
                    i += 1
                    j -= 1
                    continue
                else: 
                    return False

            return True
        except:
            print(i, j, )


        