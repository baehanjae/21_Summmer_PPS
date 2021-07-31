'''
https://leetcode.com/problems/isomorphic-strings/ 
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 각 문자를 등장 순서대로 번호를 매기고, 같은 문자끼리는 같은 번호를 매겨서, 해당 번호들의 배열이 같은 지 다른 지 판단하는 방식
        i = 0
        s_chlist = [] # s안의 문자들 모음
        s_idxlist = [] # 번호로 치환한 값들의 배열
        for x in s :
            if x in s_chlist : # 이전에 나온 문자면 s_chlist에서 해당 문자의 인덱스를 s_idxlist에 저장
                s_idxlist.append(s_chlist.index(x))
            else : # 아니라면 s_chlist에 해당 문자를 저장, s_idxlist에 i값을 저장
                s_chlist.append(x)
                s_idxlist.append(i)
                i += 1
        
        # t도 반복
        i = 0
        t_idxlist = []
        t_chlist = []
        for x in t :
            if x in t_chlist :
                t_idxlist.append(t_chlist.index(x))
            else : 
                t_chlist.append(x)
                t_idxlist.append(i)
                i += 1

        # 두 배열 비교
        return s_idxlist == t_idxlist
        
a = Solution()
s = "egg"
t = "add"
print(a.isIsomorphic(s,t))