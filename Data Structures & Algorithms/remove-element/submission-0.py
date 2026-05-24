class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_i = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[val_i] = nums[i]
                val_i += 1

        return val_i