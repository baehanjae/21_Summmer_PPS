#1.원으로 앉은 사람들을 리스트로 구성
#2.사람들을 index를 활용하여 제거  +  제거 후 담을 리스트 준비 
#3.N만큼 큰 for문 구성
#4.index는 k-1만큼 크기를 늘려 구한 후, 리스트에 담아 
#4.index >= 남아있는 사람이면 index에서 남아있는 사람을 나눈 나머지 구해

n,k=map(int, input().split())
origin=[i for i in range(1, n+1)]  #1.원으로 앉은 사람들을 리스트로 구성

res=[] #2.제거 후 담을 리스트
idx=0  #2.사람들을 index를 활용하여 제거

for i in range(n) : #3.N만큼 큰 for문 구성
    idx+=k-1 #4.index는 k-1만큼 크기를 늘려
    #4.index >= 남아있는 사람이면 index에서 남아있는 사람을 나눈 나머지 구해
    if idx >= len(origin) :
        idx=idx % len(origin)
    res.append(str(origin.pop(idx)))

print("<",", ".join(res),">",sep='')

    
