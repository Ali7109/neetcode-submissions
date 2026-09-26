class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        """

            - Find substrings
                - each letter appears in AT MOST one substring
            

            - Truth Map (Counter dictionary of string s)
                - counter = {
                    x: 3
                    y: 2
                    z: 2
                    b: 3
                    i: 1
                    s: 1
                    l: 1
                }

            - Seen Map (Counter diciontary of letters seen)
                - {

                }

            for char in s
                add char to seen_map
                have we seen counter[char] characters in seen

                r
            l
            xyxxyzbzbbisl

            curr = {}

        """
        counter = Counter(s)
        curr_set = set()
        l = 0
        lens = []

        for r in range(len(s)):
            
            curr_set.add(s[r])
            counter[s[r]] -= 1
            if counter[s[r]] == 0:
                curr_set.remove(s[r])
                if not curr_set:
                    lens.append(r-l+1)
                    l = r + 1
        
        return lens



