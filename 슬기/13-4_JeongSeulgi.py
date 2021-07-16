n = int(input())
arr = list(map(int, input().split()))

arr.append(0)
arr.append(0) 
#배열 index 때문에 2개를 추가 

cnt = 0
for i in range(n):
    if arr[i] == 1 : #반대로 모두 0이 되도록 만들어주기 위해 
        arr[i+1] = int(not(arr[i+1])) #1이면 그 다음과 
        arr[i+2] = int(not(arr[i+2])) #그 다다음의 숫자를 반대로 
        cnt += 1
           
print(cnt)

'''
13-4 방탈출 
https://www.acmicpc.net/problem/15729
'''