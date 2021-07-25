class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = sys.maxsize # 최소값을 알아내기 위한 변수

        # 최솟값과 최댓값을 계속 갱신
        for price in prices: # 리스트의 한 아이템마다 최소값과 이익을 계산
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit