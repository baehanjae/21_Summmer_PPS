'''
def fibo(N):
    if N == 1 or N == 2:
        return 1
    else:
        return fibo(N-2) + fibo(N-1)
'''
# 피보나치 재귀함수를 이용해서 구현 -> 시간 오버

def fibo(N): # DP를 이용한 피보나치 구현
    fiboList = [1,1] #1,2번째 값이 입력되어 있는 배열
    for i in range(2,N): # 입력데이터에 따라서 리스트에 추가
        fiboList.append(fiboList[i-2] + fiboList[i-1])

    return fiboList[N-1] # 최종 결과 반환


N = int(input())
print(fibo(N))