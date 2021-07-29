#한번에 올라갈 수 있는 계단의 수는 한칸 또는 두칸이며, 해당 칸을 밟을 경우 그만큼의 코스트를 사용
#최소코스트는?
#다음 칸으로 갈 때 최소 코스트: 두 칸 밑과 한 칸 밑을 비교하여 더 작은 코스트 선택 
class Solution:
    def minCostClimbingStairs(self, cost) :
        dp=[0 for i in range(len(cost)+1)]
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)) :
            onestep=dp[i-1]+cost[i]
            twostep=dp[i-2]+cost[i]
            dp[i]=min(onestep,twostep)
        return min(dp[len(cost)-2],dp[len(cost)-1])

sol1=Solution()
print(Solution.minCostClimbingStairs(sol1,[10,15,20]))

sol2=Solution()
print(Solution.minCostClimbingStairs(sol2,[1,100,1,1,1,100,1,1,100,1]))


"""
동적프로그래밍
작은 부분문제은 한번만 품 (정답을 구한 작은 문제들을 메모 후 그보다 큰 문제를 풀어나갈 때 똑같은 작은 문제가 나타나면 작은 문제의 결과값을 이용)
조건
작은 문제가 반복이 일어나는 경우, 같은 문제는 구할 때마다 정답이 같음

"""
