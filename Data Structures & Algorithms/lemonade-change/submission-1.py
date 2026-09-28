class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {
            5: 0, 10:0, 20:0 
        }

        for b in bills:
            
            cash[b] += 1
            change = b - 5

            if change == 15:
                if cash[10] and cash[5]:
                    cash[10] -= 1
                    cash[5] -= 1
                elif cash[5] >= 3:
                    cash[5] -= 3
                else:
                    return False
            elif change == 10:
                if cash[10]:
                    cash[10] -= 1
                elif cash[5] >= 2:
                    cash[5] -= 2
                else:
                    return False
            elif change == 5:
                if cash[5]:
                    cash[5] -= 1
                else:
                    return False
        return True