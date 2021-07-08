class Solution:
    def dayOfYear(self, date: str) -> int:
        tmp = date.split('-') #'-'를 기준으로 split해서 tmp list를 만들기 
        year = int(tmp[0])
        month = int(tmp[1])
        day = int(tmp[2])
        
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #월별로 며칠씩 존재하는지 list로 만들기 
        days = [int (i) for i in days] #str 리스틀 int로  
        
        ans = 0
        ans = sum(days[:month-1])+day # ex)7월 26일이면 6월까지 days를 더하고 + 26
        
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month >2: #윤년일 조건 and 2월 이후 
            ans += 1
        
        return ans

print(Solution.dayOfYear("","2019-01-09"))

'''
5-4 Day of the Year
https://leetcode.com/problems/day-of-the-year/
'''