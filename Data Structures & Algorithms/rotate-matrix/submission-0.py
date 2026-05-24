class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        """

        temp = 1
        3 1
        4 2
        [[7,2,1],[4,5,6],[9,8,3]]
        i = 1
        l = 1
        r = 1
        t = 0
        b = 2

        7 2 1
        4 5 6
        9 8 3

        """
        l, r = 0, len(matrix) - 1
        while l <= r:
            t, b = l, r
            for i in range(r-l):

                temp = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = temp

            l += 1
            r -= 1