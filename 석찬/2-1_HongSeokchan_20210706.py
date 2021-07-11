'''
https://www.acmicpc.net/status?user_id=hsch01&problem_id=4659&from_mine=1 
'''
v = 'aeiou'
while True :
    suit = True
    vnum = 0

    s = input()
    if s == 'end' : break
    for i in range(len(s)-2) : 
        if s[i] in v and s[i+1] in v and s[i+2] in v : #모음이 3개 연속 나오는지 확인
            suit = False
        elif s[i] not in v and s[i+1] not in v and s[i+2] not in v : #자음이 3개 연속 나오는지 확인
            suit = False
    for i in range(len(s)-1) :
        if s[i] == s[i+1] and s[i] not in 'eo' and s[i+1] not in 'eo' : #ee oo가 아닌 같은 글자 두 번 연속이 있는지 확인
            suit = False
    for ch in s : # 자음이 하나 이상있는지 확인
        if ch in v :
            vnum += 1
    if vnum <= 0 :
        suit = False
    
    if suit == False :
        print("<%s> is not acceptable."%s)
    else : print("<%s> is acceptable."%s)
