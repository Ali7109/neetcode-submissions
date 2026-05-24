from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)

        for char in t:
            if char not in s_counter or s_counter[char] <= 0:
                return False
            s_counter[char] -= 1
            if s_counter[char] == 0:
                del s_counter[char]
        
        return len(s_counter) == 0