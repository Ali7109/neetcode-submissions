class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        """

            1, 2, 3
            7, 1, 3
            7, 3, 4

            7, 2, 3

            6:  1, 2, 3
            11: 7, 1, 3
            14: 7, 3, 4
            
            [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
            2, 7, 5
            

        """
        
        t1, t2, t3 = target
        f1, f2, f3 = False, False, False

        for x, y, z in triplets:
            if x > t1 or y > t2 or z > t3:
                continue
            
            f1 = (f1 or x == t1)
            f2 = (f2 or y == t2)
            f3 = (f3 or z == t3)


        return (f1 and f2 and f3)