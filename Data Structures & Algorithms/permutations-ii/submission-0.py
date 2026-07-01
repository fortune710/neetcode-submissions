class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        selected = [False for _ in range(len(nums))]

        def backtrack(index: int, path: List[int]):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for idx in range(len(nums)):
                if selected[idx] or (idx > 0 and nums[idx] == nums[idx - 1] and not selected[idx - 1]):
                    continue

                path.append(nums[idx])
                selected[idx] = True
                backtrack(idx, path)

                path.pop()
                selected[idx] = False

        backtrack(0, [])
        return result
