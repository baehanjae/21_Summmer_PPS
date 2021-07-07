class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        // 주어진 list를, 각 원소의 길이를 기준으로 오름차순 정렬한다.
        strs.sort(key=lambda x : len(x))
        
        // strs가 비어있는 경우에는 ""을 리턴한다.
        if len(strs) == 0:
            return ""
        else:
            // 가장 짧은 원소(strs[0])을 기준으로 다른 원소들을 차례대로 비교한다.
            // 비교할 때, 가장 짧은 원소의 index와 같은 지 확인한다.
            // common prefix가 생기지 않는 index 까지 잘라서 return 한다.
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return strs[0][:i]
            return strs[0]
        