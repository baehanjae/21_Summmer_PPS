N = int(input())
slist = []
for i in range(N): #
    slist.append(input())

#slist = ['ABCD','145C','A','A910','Z321']

def sumstr(ostr): # 
    sum = 0
    for i in ostr:
        if i.isdigit():
            sum += int(i)

    return sum

def diff(ostr, tstr):
    j = 0
    for i in ostr:
        if i == tstr[j]:
            j += 1
        elif i > tstr[j]:
            temp = slist[j]
            slist[j] = slist[j + 1]
            slist[j + 1] = temp

for i in range(len(slist)):
    for j in range(len(slist)-i-1):
        if len(slist[j]) > len(slist[j+1]): # str의 길이로 비교
            temp = slist[j]
            slist[j] = slist[j+1]
            slist[j+1] = temp
        elif len(slist[j]) == len(slist[j+1]):# str의 길이가 같을 경우
            if sumstr(slist[j]) > sumstr(slist[j+1]): # 숫자의 합으로 비
                temp = slist[j]
                slist[j] = slist[j + 1]
                slist[j + 1] = temp

            elif sumstr(slist[j]) ==  sumstr(slist[j+1]):# 교숫자의 합이 같을 경우
                k = 0
                for z in slist[j]: # 사전순으로 정렬 
                    zsmall = z.lower()
                    slistsmall = slist[j+1][k].lower() # 모든 문자 소문자화 

                    if zsmall == slistsmall: # 비교하는 문자열들이 같은 글자일 때 
                        k += 1

                    elif zsmall.isdigit() and slistsmall.isalpha(): # 숫자와 문자를 비교했을 경우 
                        temp = slist[j]
                        slist[j] = slist[j + 1]
                        slist[j + 1] = temp

                    elif zsmall > slistsmall: # 사전순으로 뒤에 있을 경우 
                        temp = slist[j]
                        slist[j] = slist[j + 1]
                        slist[j + 1] = temp
                        break


for i in slist:
    print(i)
