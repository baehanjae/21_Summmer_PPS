class Solution:
    def floodFill(self, image, sr, sc, newColor) :
        R, C = len(image), len(image[0])
        color = image[sr][sc] #image[sr][sc]의 색을 저장
        if color==newColor : #image[sr][sc]의 색과 newColor가 같으면 
            return  image #그대로 image 리턴

        def dfs(r,c) :
            #image[sr][sc] 기준으로 북, 남, 서, 동  쪽 좌표 순으로 확인 (재귀함수로 구현)
            if image[r][c]==color : #해당 image[r][c]가 image[sr][sc]와 색이 같다면 
                image[r][c]=newColor #색을 newColor로 바꿈
                #해당 image[r][c] 기준으로 북, 남, 서, 동쪽 좌표에 newColor로 바꾸어야 하는 경우가 있는지 확인
                if r>=1 : #북쪽 좌표 존재한다면
                    dfs(r-1,c)
                if r+1 < R : #남쪽 좌표 존재한다면
                    dfs(r+1,c)
                if c>=1 : #서쪽 좌표 존재한다면
                    dfs(r,c-1)
                if c+1<C : #동쪽 좌표 존재한다면
                    dfs(r,c+1)
                    
        dfs(sr,sc) #image[sr][sc]의 색과 newColor가 다르면 dfs 함수 호출 
        return image

sol1=Solution()
print(Solution.floodFill(sol1, [[0,0,0],[0,0,0]], 0, 0, 2))

#손으로 적어가면서 상황을 살펴보면 이해가 잘 감
#출처: https://leetcode.com/problems/flood-fill/solution/
