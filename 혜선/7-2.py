d={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','0':'zero'}
m,n= map(int,input().split())

res=[] # 2차원 리스트로 활용 예정 [  [숫자, 영어 표현] ......  ]

for i in range(m, n+1) : # 입력받은 두 숫자 사이에 대해 반복문 돌려 
    s=''
    for j in str(i) : # 각 숫자를 str로 변환 후, 각 자리의 수에 대해 반복문 돌려 
        s+=d[j] # 각 자리 수(key)에 대응하는 영어 표현(value) 찾아서 문자열 생성
    res.append([i,s]) # 리스트에 추가 
res.sort(key=lambda x:x[1]) # 리스트의 두번째 요소 기준으로 정렬

for i in range(len(res)) :
    if i%10 == 0 and i!=0:
        print()
    print(res[i][0],end=" ")

