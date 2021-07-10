class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: # num이 1이면 true
            return True
        if num < 4: # num이 1이 아니고 4보다 작으면 아님
            return False
        while num % 4 == 0: # num을 4로 나눈 나머지가 0일 때만 = 4의 거듭제
            num /= 4 # num = 4^n
            if num == 1: #num이 1이면 4^0
                return True
        return False

'''
Power of Four
https://leetcode.com/problems/power-of-four/
'''
