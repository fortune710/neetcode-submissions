class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = i + 1

        array_end = len(numbers) - 1

        #i less than array_end because i and j must not be same
        #meaning j will be array_end while i 1 less than array_end
        while i < array_end:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1] 

            if j >= array_end:
                i += 1
                j = 1 + i
            else:
                j += 1

