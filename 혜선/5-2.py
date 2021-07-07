num=int(input())
res_list=[] 
for i in range(num) : 
    eq=input() #각 식 입력 
    length=len(eq) # 각 식의 총 길이 
    res=0 #각 식의 결과
    digit='' #숫자 부분만 추출 
    for j in range(length) :
        if eq[j].isdigit() or eq[j]=='.' : #각 자리 수가 숫자이거나 소수점이면
            digit+=eq[j] # 숫자 부분 변수에 담아 
        else : #각 자리 수가 특수문자이면
            if eq[j-1].isdigit() : #처음으로 특수문자 등장 시
                res+=float(digit) # res를 숫자 부분으로 초기화
            #각 특수문자 상황에 따라 계산 
            if eq[j]=='@' : 
                res*=3
            if eq[j]=='%' :
                res+=5
            if eq[j]=='#' :
                res-=7
    res_list.append(round(res,2)) #res를 list에 저장

for i in range(num) :
    print("{:.2f}".format(res_list[i])) # 소수점 둘째 자리까지 출력 
    
        
    
    
