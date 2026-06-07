class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index: int, path: List[int], currentSum: int):
            if currentSum == target:
                result.append(path[:])
                return
            
            if index == len(nums) or currentSum > target:
                return

            path.append(nums[index])
            backtrack(index, path, currentSum + nums[index])

            path.pop()
            backtrack(index + 1, path, currentSum)

        backtrack(0, [], 0)
        return result

        