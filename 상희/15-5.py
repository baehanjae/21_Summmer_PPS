class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls=len(s)
        if ls==0:
            return True
        i=0
        
        for c in t:
            if c == s[i]:
                i+=1
                if i==ls:
                    return True 
        return False
