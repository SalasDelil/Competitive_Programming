class Solution:
    def totalMoney(self, n: int) -> int:
        total_amount = 0
        daily_value = 1
        inc_value = 0
        day = 1
        i = 0

        while i < n:
            if day <= 7:
                total_amount += (daily_value + inc_value)
                daily_value += 1
                day += 1
                i += 1
            else:
                inc_value += 1
                daily_value = 1
                day = 1
        
        return total_amount