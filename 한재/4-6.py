class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while True:  # 반복문 실행
            if num < 10:  # 종료 조건
                break

            else:
                # 한자리씩 숫자를 나누기 위해서,,,
                sum = 0 # 계산을 위한 변수
                num = str(num) # 정수를 문자열로 변환 후 for 문 사용
                for i in num:
                    sum += int(i)
                num = sum # 다시 while이 실행되기 떄문
                sum = 0 # 다음에 else로 들어오는 경우를 대비

        return num


'''
한자리씩 숫자를 나누는거,,,
- 문자열을 사용하면 쉽게 된다. 
https://leetcode.com/problems/add-digits/submissions/
'''