class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            if not arr1:
                return arr2
            elif not arr2: 
                return arr1
            
            l1, l2 = 0, 0
            merged = []

            while l1 < len(arr1) and l2 < len(arr2):
                n1, n2 = arr1[l1], arr2[l2]
                if n1 <= n2:
                    merged.append(n1)
                    l1 += 1
                else:
                    merged.append(n2)
                    l2 += 1

            while l1 < len(arr1):
                merged.append(arr1[l1])
                l1 += 1

            while  l2 < len(arr2):
                merged.append(arr2[l2])
                l2 += 1
            
            return merged
        
        def merge_sort(arr):
            if len(arr) == 1:
                return arr

            mid_idx = len(arr) // 2
            sorted_left = merge_sort(arr[:mid_idx])
            sorted_right = merge_sort(arr[mid_idx:])
            return merge(sorted_left, sorted_right)
            
        return merge_sort(nums)
