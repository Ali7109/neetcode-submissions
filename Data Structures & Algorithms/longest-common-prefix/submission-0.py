class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)

        if not strs:
            return ""

        max_i = 0
        
        for i in range(len(strs[0])):
            match = True
            for s in strs:
                if s[i] != strs[0][i]:
                    match = False
                    break
            if match:
                max_i += 1
            else:
                break
                    
            
        return "".join(strs[0][:max_i])