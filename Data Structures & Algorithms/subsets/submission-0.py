class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(index: int, path: List[int]):
            ## Base Case
            if index == len(nums):
                result.append(path[:])
                return

            ## No Constraints

            ## Move To Next Step
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            backtrack(index + 1, path)

        backtrack(0, [])
        return result
            
