N, M = map(int, input().split())
arr = list(map(int,input().split()))
result = 0
for i in range(N): # 첫번쨰 카드
    for j in range(i+1,N): # 두번쨰 카드
        for k in range(j+1, N): # 세번째 카드
            if arr[i] + arr[j] + arr[k] > M: # 제한을 넘을 경우
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k]) # 그렇지 않은 경우
print(result)

#knapsack이 떠오른 문제
#하지만 3장으로 골라야하는 카드수가 정해져 있기 때문에 각각의 경우를
#branch and bound 로 풀어주면 된다.