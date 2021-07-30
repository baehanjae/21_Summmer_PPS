import sys

# inf = open('input.txt');
inf = sys.stdin

T = inf.readline()
print(T)

for t in range(0, int(T)):

    Answer = 0 # 정답을 적을 변수
    dic = {} # 해당 숫자별 빈도를 기록하는 dictionary

    N = inf.readline() # 들어오는 인풋 값 확인

    # istr = list(map(int,inf.readline().split()))
    istr = inf.readline().split() # 입력값 리스트
    for i in range(len(istr)): # str을 int로 형 변환 (map이 테스트 케이스를 통과하지 못하는 것 같음,,,)
        istr[i] = int(istr[i])

    for i in istr: # 빈도 측정
        if i in dic.keys(): # 이미 딕셔너리 안에 해당 값이 존재하면 빈도 추가
            dic[i] += 1
        else: # 딕셔너리 안에 해당 값이 없다면 새로 신설
            dic[i] = 1

    for s in dic.keys(): # 홀짞 확인 및 연산 수행
        if dic[s] % 2 == 0: # 짝수번 나온 경우, 반복문 계속 실행
            continue
        else: # 홀수번 나온 경우, 직전에 연산된 값과 XOR 연산 후 저장
            Answer ^= s # 0 ^ x = x 라는걸 이용하기에 최초에 연산에도 문제없음

    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()

'''
알고리듬 설계 포인트
1. 홀수 인지 짝수 인지 확인
    딕셔너리 사용 
    짝수는 버리기
2. Xor 연산
    홀수로 판별된 수들은 ^(XOR) 바로바로 연산
3. 문제 사이트
https://www.codeground.org/practice/practiceProblemViewNew
어려웠던점 
코드그라운드가 테스트 코드가 없어서 쉬운 문제인데 시간을 많이 사용함,,,
'''