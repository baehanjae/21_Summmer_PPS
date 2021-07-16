'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # ex) s = [a, b, c, d, e, f, a, a, b, b, c, d, b]
        tmp = list(set(s)) #중복 문자 제거 
        # tmp = [a, b, c, d, e, f]
        
        cnt = 0
        isOdd = 0
        for i in tmp: 
            if s.count(i) % 2 == 0: #짝수면 
                cnt += s.count(i) #그 수만큼 더하고 
            elif s.count(i) % 2 != 0 and s.count(i) > 1 : #홀수인데 3개 이상이면 
                cnt += (s.count(i) - 1) #가운데 들어갈 수 있는 경우를 제외하고 더한다 
                isOdd += 1 #가운데 들어갈 수 있는 경우의 수 
            elif s.count(i) == 1: #홀수이고 1개이면 가운데 밖에 못들어간다 
                isOdd += 1 #가운데 들어갈 수 있는 경우의 수 
        
        # a : 3 , b : 4, c : 2, d : 2, e : 1, f : 1  
        
        if isOdd >= 1:
            cnt += 1 
        
        return cnt
'''

'''
20-4 Longest Palindrome
https://leetcode.com/problems/longest-palindrome/
'''