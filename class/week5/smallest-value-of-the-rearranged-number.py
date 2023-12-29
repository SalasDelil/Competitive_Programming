class Solution:
    def smallestNumber(self, num: int) -> int:
        digits  = [num for num in str(num)]
        
        if num < 0:
            for i in range(1, len(digits)-1):
                for j in range(i, len(digits)):
                    if digits[j] > digits[i]:
                        digits[i], digits[j] = digits[j], digits[i]

            rearranged_num = "".join(digits)

            return int(rearranged_num)
        else:
            for i in range(len(digits)-1):
                for j in range(i, len(digits)):
                    if digits[j] < digits[i]:
                        digits[i], digits[j] = digits[j], digits[i]
            
            for k in range(len(digits)):
                if digits[k] != "0":
                    digits[0], digits[k] = digits[k], digits[0]
                    break

            rearranged_num = "".join(digits)

            return int(rearranged_num)
