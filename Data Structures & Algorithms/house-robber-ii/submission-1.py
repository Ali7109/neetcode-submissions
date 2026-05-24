class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_helper(nums):

            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                return max(nums)
            
            prev = nums[0]
            prev2 = 0

            for num in nums[1:]:
                temp = prev
                prev = max(prev, prev2+num)
                prev2 = temp
            
            return prev
        
        total1 = rob_helper(nums[1:])
        total2 = rob_helper(nums[:len(nums)-1])

        return max(total1, total2, nums[0])