'''
https://leetcode.com/problems/student-attendance-record-i/submissions/
'''

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ab = 0 #결석 횟 수
        for i in range(len(s)) :
            if i < len(s)-2 : # i가 len(s)-2 일 때
                if s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L' : #현재 char부터 L이 연속 3번 나오는지 확인 / 맞다면 return False
                    return False
            if s[i] == 'A' : #A가 나오면 A가 몇 번 나왔는지 counting / A가 2개 이상 나오면 return False
                ab = ab+1
                if ab >= 2 :
                    return False
        return True # 위의 조건문들에서 걸러지지 않으면 return True

'''
s = input("")
obj = Solution()
print(obj.checkRecord(s))
'''
