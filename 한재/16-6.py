class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        cr = []  # check redundancy 중복 검사용 리스트
        while True:
            strn = str(n) # 수자를 문자열로 : digit으로 편하게 바꾸기 위해서
            sum = 0 # 최종값
            for i in strn: # 한 digit씩 반복
                n = int(i) ** 2 # 제곱
                sum += n

            n = sum
            if n in cr: # 중복체크, 중복 : 계속 반복될복것이다.
                return False

            cr.append(n) # 중복체크 리스트에 추가

            if sum == 1: # 조건만족
                return True


