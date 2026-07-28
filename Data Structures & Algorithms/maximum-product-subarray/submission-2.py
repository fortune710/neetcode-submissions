import sys
sys.setrecursionlimit(20000) # Set this higher than the length of nums

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cache = {}
        n = len(nums)
        self.ans = 0

        if n == 1:
            return nums[0]

        def travel(i):
            if i == 0:
                return (nums[0], nums[0])
            
            if i in cache:
                return cache[i]
            
            prev_min, prev_max = travel(i - 1)
            
            # Calculate your 3 options
            option1 = nums[i]
            option2 = nums[i] * prev_max
            option3 = nums[i] * prev_min
            
            curr_min = min(option1, option2, option3)
            curr_max = max(option1, option2, option3)
            
            # Update a global result here!
            self.ans = max(self.ans, curr_max)
            
            cache[i] = (curr_min, curr_max)
            return cache[i]
    
        travel(n - 1)
        return self.ans
        
