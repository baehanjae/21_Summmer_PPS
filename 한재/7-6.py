def swap(ilist, i): # 스왑 평션
    temp = ilist[i]
    ilist[i] = ilist[i + 1]
    ilist[i + 1] = temp

N = int(input())
ilist = [] # 리스트 형태로 입력값을 넣을 배열 선언
for i in range(N):
    ilist.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N-i-1):
        if ilist[j][0] > ilist[j+1][0]: #앞부분 먼저 비교 
            swap(ilist,j)

        elif ilist[j][0] == ilist[j+1][0]: # 뒷부분 비교 
            print(ilist[j][1], ilist[j + 1][1])
            if ilist[j][1] > ilist[j+1][1]:
                swap(ilist,j)

print(ilist)

#좌표 정렬하기
