class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c='qwertyuiopasdfghjklzxcvbnm'
        res=2**31-1
        for n in c:
            index = s.find(n)
            if index ==-1:
                continue
            if s[index+1:].find(n)==-1:
                res=min(res,index)
        return res if res!=2**31-1 else -1
