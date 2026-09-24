class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        """
        
            gas =  [1, 2, 3, 4]
            cost = [2, 2, 4, 1]
                    ^
            curr_g = gas[i] - cost[i]

                    -1 0  -1 3

            1, 2, 3
            2, 3, 2
            -1 -1 1

            
            g_c = [-1, -1, 1]

            gas=[1,2,3,4,5]
            cost=[3,4,5,1,2]
            -2 -2 -2 3 3

        """
        if sum(gas) - sum(cost) < 0:
            return -1
        start_idx = 0
        curr_gas = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            curr_gas += (g-c)
            if curr_gas < 0:
                start_idx = i + 1
                curr_gas = 0

        return start_idx
