vowelList = ['a', 'e', 'i', 'o', 'u']

while True : 
    password = input() 
    if password == 'end' : break #end일 시 break

    uppercase = False
    for word in password :
        if word.isupper() : uppercase = True # 대문자 포함 여부 확인

    if len(password) > 20 or len(password) < 1  or uppercase: # 문자열이 한글자 이상 20글자 이하가 아니거나 대문자를 포함하면 문자열 다시 받음
        continue
    
    checkVOWEL = False
    continuity = 0
    preword = ''
    proper = True

    for word in password : #문자열에서 한 문자씩 비교
        if word == preword and word+preword != 'ee' and word+preword != 'oo' : proper = False #같은 글자가 연속적으로 두번 오면 proper=false (ee 와 oo는 제외).
        if word in vowelList : #해당 문자가 모음일 때
            checkVOWEL = True 
            if preword in vowelList : #이전 문자가 모음이면 continuity + 1
                continuity = continuity + 1
            else : continuity = 0 #자음이면 continuity = 0
        else : #해당 문자가 자음일 때
            if preword not in vowelList : #이전 문자가 자음이면 continuity + 1
                continuity = continuity + 1
            else : continuity = 0 #모음이면 continuity = 0
        preword = word #다음 문자로 넘어가기전 현재 문자를 이전 문자로 설정
        if continuity > 1 : proper = False #같은 문자가 3번 이상 나오면 proper = False

    if checkVOWEL == False : proper = False #모음이 없었으면 proper = False

    if proper :
        print("<%s> is acceptable."%password)
    else :
        print("<%s> is not acceptable."%password)
    