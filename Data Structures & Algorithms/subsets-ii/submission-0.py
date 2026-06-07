class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(index: int, path: List[int]):
            if index == len(nums):
                result.append(path[:])
                return

            path.append(nums[index])
            backtrack(index + 1, path)

            path.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
                
            backtrack(index + 1, path)

        backtrack(0, [])
        return result
