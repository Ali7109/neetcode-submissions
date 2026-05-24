class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Linear time solution with O(n) space, we keep track of a counter
        # NlogN time solution with O(1) space, we sort the array and keep track of the counts
        
        # Boyer-Moore Voting Algorithm
        # - Choose a candidate
        # - When you see the candidate, increment
        # - When you dont, decrement
        # - If the candidate's count reaches 0, choose current element to be candidate

        # nums = [5, 5, 1, 1, 1, 5, 5]
        #        1, 2   
        #       
        # nums = [2, 2, 2, 2, 3, 3, 3]
        #        candidate, cnt = 2, 0
        candidate, cnt = None, 1

        for num in nums:
            if candidate != num:
                cnt -= 1
            else:
                cnt += 1
            
            if cnt == 0:
                candidate = num
                cnt = 1
        
        return candidate
