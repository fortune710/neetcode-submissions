class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        n = len(nums)
        max_length = 1

        def checkLength(index: int):
            if index == n:
                return 0

            if index in cache:
                return cache[index]

            count = 1
            for i in range(index + 1, n):
                if nums[i] > nums[index]:
                    count = max(count, 1 + checkLength(i))

            cache[index] = count
            return count

        for index in range(n):
            max_length = max(max_length, checkLength(index))

        return max_length

