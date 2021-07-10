def solution(number, k):
    #값을 저장해줄 스택 생성
    x = [] 
    
    #입력 받은 값 중에 가장 큰 수가 앞으로 가게끔 스택에 저장
    for i in number:
        while x and x[-1] < i and k > 0:
            x.pop()
            k -=1
        x.append(i)
    
    #k가 0이 아닌 경우에는 뒤에서 부터 남은 k 수 만큼 스택에서 빼기
    while k > 0:
        x.pop()
        k-=1
    
    answer = "".join(x)
    return answer