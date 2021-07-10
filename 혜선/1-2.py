def solution(skill, skill_trees):
    answer=0 #가능한 스킬트리 총 개수 
    for i in range(len(skill_trees)) :
        skill_str='' #skill에 해당하는 글자부분만 추출하여 만든 문자열
       
        for j in range(len(skill_trees[i])) : #skill_trees의 각 원소에 대해 
            if skill_trees[i][j] in skill : #skill_trees의 각 원소의 각 글자가 skill에 있으면 
                skill_str+=skill_trees[i][j] #skill_str에 추가 

        check_list=[] 
        idx=len(skill) 
        for j in range(len(skill)) : #skill의 각 글자가 
            for z in range(len(skill_str)) : # skill_str에서는 몇 번째 인덱스에 있는지 확인 
                if skill[j]==skill_str[z] : # 해당 글자가 skill_str에 있으면 
                     check_list.append(z) # 해당 인덱스를 check_list에 보관
                     break
                if skill[j]!=skill_str[z] and z==len(skill_str)-1: # 해당 글자가 skill_str에 끝내 없는 경우
                    #idx: 해당 글자가 skill_str에 끝내 없는 경우 보관할 인덱스 (skill의 길이 이상으로 정하여 다른 인덱스와 겹칠 일 없게 함)
                    check_list.append(idx) 
                    idx+=1
                    
        #check_list가 ascending sort인 경우만 가능한 스킬트리임
        isAscending=True 
        for j in range(1,len(check_list)) :
            if check_list[j] < check_list[j-1] :
                isAscending=False
        if isAscending==True :
            answer+=1
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
print(solution("AC", ["A", "CD", "BAC", "CA"]))
