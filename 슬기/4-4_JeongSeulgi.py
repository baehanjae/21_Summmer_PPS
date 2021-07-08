'''
k층 n호에는 
k-1층 1호 - n호까지 사는 사람들의 수의 합 만큼 거주 
0층은 호실 번호대로 거주 
'''
realans = list() 
n = int(input())
for i in range(n):
    k = int(input())
    n = int(input())
    
    ans = [j for j in range(1, n+1)] #0층 
    for l in range(k):
        for m in range(1, n):
            ans[m] += ans[m-1] #ex)2층 5호에 사는 사람은 0층 1-5호 + 1층 1-5호 사는 사람들 수 만큼 있어야 하므로 
    realans.append(ans[-1]) #최종답을 리스트에 넣어서 

for i in realans:
    print(i) #한번에 출력

'''
4-4 부녀회장이 될테야 
https://www.acmicpc.net/problem/2775
'''
