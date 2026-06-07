class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        selected = [False for _ in range(len(nums))]

        def backtrack(index: int, path: List[int]):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if selected[i]:
                    continue

                path.append(nums[i])
                selected[i] = True
                backtrack(i + 1, path)

                path.pop()
                selected[i] = False

        backtrack(0, [])
        return result
