'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t): #정렬을 했을 때 값이 같으면 
            return True
        else :
            return False
'''

'''
17-4 Valid Anagram
https://leetcode.com/problems/valid-anagram/
'''