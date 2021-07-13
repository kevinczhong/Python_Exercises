class Solution():
    def isPrime(self, year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True
    
    def findMonthDays(self, month, year):
        longmonth = [1, 3, 5, 7, 8, 10, 12]
        month_count = longmonth.count(month)
        if month == 2:
            if self.isPrime(year) is True:
                return 29
            else:
                return 28
        elif month_count > 0:
            return 31
        else:
            return 30
    
s = Solution()
print(s.findMonthDays(11, 2020))