word=input()
length=len(word) # 총 길이
numOfTimes=length//10  #10번씩 끊어서 나올 수 있는 횟수 
remainder=length%10 #나머지

for i in range(numOfTimes) : #10개씩 끊어서 출력 
    print(word[10*i:10*(i+1)])

if remainder!=0 : #10의 배수가 아닌 경우
    print(word[numOfTimes*10:])
