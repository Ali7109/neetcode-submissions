class Solution:
    def checkValidString(self, s: str) -> bool:
        """

            ( ( * * ) 

            ( ( '' ) )


            (((*)
            o = [0, 1]
            w = [3]


            (**)
            o = [0]
            w = [1, 2]



            )

            o = []
            w = [0]

            
            
        """
        o = []
        w = []
        for i, val in enumerate(s):
            if val == "(":
                o.append(i)
            elif val == "*":
                w.append(i)
            else:
                if o:
                    o.pop()
                elif w:
                    w.pop()
                else:
                    return False
        while o and w:
            if w[-1] > o[-1]:
                o.pop()
            w.pop()
        return len(w) >= len(o)
                
