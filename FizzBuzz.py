class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        m = int(n)
        for val in range(1, m + 1):
            if val % 3 == 0 and val % 5 == 0:
                arr = "FizzBuzz"
                answer.append(arr)
            elif val % 3 == 0:
                arr = "Fizz"
                answer.append(arr)
            elif val % 5 == 0:
                arr = "Buzz"
                answer.append(arr)
            else:
                str_val = str(val)
                answer.append(str_val)
        return answer
