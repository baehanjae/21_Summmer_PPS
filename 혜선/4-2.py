num=input()
for i in range(len(num)) :
    if(num[i]==' ') : #공백 찾아
        idx=i
        break
#공백 기준으로 첫번째 operand 두번째 operand 추출
a=int(num[:idx])
b=int(num[idx+1:])
res=a+b
print(res)
