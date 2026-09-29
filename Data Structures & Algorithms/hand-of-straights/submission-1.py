class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        """

            1, 2, 2, 3, 3, 4, 4, 5

        """

        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        counter = Counter(hand)
        count = 0 

        for num in hand:
            end = num + groupSize

            i = num
            while i < end:
                if i in counter:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]
                else:
                    break
                i += 1
            if i == end:
                count += 1
        print(counter)
        return len(counter) == 0 and count == len(hand)//groupSize