test = int(input())
ans = list()

for i in range (1, test+1):
    a = list(map(int, input().split()))
    avg = sum(a[1:])/a[0] #평균 계산 (a[0]는 인원 수)
    cnt=0
    for j in range (1, len(a)):
        if(a[j]>avg):
            cnt+=1
    ans.append(round(cnt/a[0]*100, 3)) #비율 계산

for i in range (0, test): #다 끝나고 출력되도록
    print("{:.3f}%".format(ans[i])) #소숫점 맞춰주기 

'''
1-4 평균은 넘겠지
https://www.acmicpc.net/problem/4344
'''