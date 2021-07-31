'''
https://leetcode.com/problems/divisor-game/submissions/ 
'''
class Solution:
    def divisorGame(self, n: int) -> bool:
        cnt = 0
        while n > 1 :
            divisor = []
            for i in range(1,n) :
                if i != n and n % i == 0 :
                    divisor.append(i) # 약수를 구하여 리스트에 저장
            n -= divisor[0] # 첫 번째 약수를 n에서 뺌
            cnt += 1
        
        #Alice는 1,3,... 번째에 게임을 하고, Bob은 2,4,... 번째에 게임을 하므로
        # 1이 되어 게임이 끝났을 때 Bob이 마지막으로 끝났으면 다음 차례인 Alice 아웃,
        # Alice가 마지막으로 끝났으면 다음 차례인 Bob 아웃
        if cnt % 2 == 0 : 
            return False
        else :
            return True

a = Solution()
n = 3
print(a.divisorGame(n))