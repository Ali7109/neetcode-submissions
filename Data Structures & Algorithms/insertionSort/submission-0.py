# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        n = len(pairs)
        res = [] # list of states

        for i in range(n):
            j = i - 1
            for j in range(i-1, -1, -1):
                if pairs[j].key > pairs[j+1].key:
                    pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                else:
                    break
            res.append(pairs[:])
            
        return res
