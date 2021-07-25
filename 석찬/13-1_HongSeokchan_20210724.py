'''
https://www.acmicpc.net/problem/11047 
'''
N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
ans = 0
for i in range(len(coins)-1,-1,-1) : # 입력된 동전 중 큰 수 부터 내려오기
    if K >= coins[i] : #해당 수가 K보다 작을 때
        quo = K//coins[i]
        ans += quo
        K = K - coins[i]*quo
    if K == 0 : break
print(ans)
