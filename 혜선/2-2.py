num=int(input())

res_list=[] # 각 testcase 결과 보관용 리스트

for i in range(num) :
    testCase=input()
    length=len(testCase)
    res=0 # 결과
    for j in range(length) :
        cnt=0 # 연속된 'O' 의 개수
        if testCase[j]=='O' : #'O'이 나오면
            z=j
            while 0<=z: 
                if testCase[z]=='O' :
                    cnt+=1
                else :
                    break
                z-=1
            res+=1*cnt
    res_list.append(res)

for i in range(num) :
    print(res_list[i])
