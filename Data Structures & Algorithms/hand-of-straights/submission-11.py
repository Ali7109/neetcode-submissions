class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        """

            1, 2, 2, 3, 3, 4, 4, 5

        """

        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        counter = Counter(hand)
        for card in hand:
            if counter[card] == 0: continue
            num_of_groups = counter[card]

            for i in range(card, card + groupSize):
                if counter[i] < num_of_groups:
                    return False
                counter[i] -= num_of_groups # remove number of groups this number will be in 
        
        return True # found all numbers enough to complete groups