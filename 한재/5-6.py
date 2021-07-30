class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ns = [] # 알파벳 소문자로 바꾸기 위한 배열
        for i in s:
            if i.isalpha() or i.isdigit():
                ns.append(i.lower())
        for i in range(len(ns) // 2):
            if ns[i] != ns[-(i + 1)]: # 규칙에 어긋나면 False 리턴
                return False
        return True # 한번도 규칙에 어긋나지 않았다면 True 리턴
'''
3 : 0 1 2 if i = 1 (3 // 2)
4 : 0 1 2 3  i = 2 (4 // 2)

막혔던 것,
1. 공백, 알파벳아닌문자 제거
-> digit,alpha 인것만 모아서 새롭게 문자열 만듬

https://leetcode.com/problems/valid-palindrome/submissions/
'''