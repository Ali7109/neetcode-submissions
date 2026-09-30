class Solution:
    def checkValidString(self, s: str) -> bool:
        
        o = []
        w = []

        for i, c in enumerate(s):
            if c == "(":
                o.append(i)
            elif c == "*":
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
        
