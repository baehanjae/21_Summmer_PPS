class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        fiboList = [0, 1]  # 0,1번째 값이 입력되어 있는 배열
        for i in range(2, n + 1):  # 입력데이터에 따라서 리스트에 추가
            fiboList.append(fiboList[i - 2] + fiboList[i - 1])

        return fiboList[n]  # 최종 결과 반환