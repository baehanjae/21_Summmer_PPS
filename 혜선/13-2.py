#-를 기준으로 split한다.
#각 원소 내에서 '+'가 있다면, '+"를 기준으로 split한 후
#첫번째 원소였다면, res+=
#첫번째 원소가 아니라면, res-=

eq=input().split('-')
res=0

for i in eq[0].split('+') :
    res+=int(i)
for i in eq[1:] :
    for j in i.split('+') :
        res-=int(j)
print(res)
