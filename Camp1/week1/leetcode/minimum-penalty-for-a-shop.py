class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        min_penality = float("inf")
        earliest_hour = 0
        y_count = customers.count("Y")
        n_count = 0

        for i in range(n + 1):
            if i < n and customers[i] == "N":
                if y_count + n_count < min_penality:
                    min_penality = y_count + n_count
                    earliest_hour = i
                n_count += 1

            if i < n and customers[i] == "Y":
                if y_count + n_count < min_penality:
                    min_penality = y_count + n_count
                    earliest_hour = i
                y_count -= 1

            if i == n:
                if y_count + n_count < min_penality:
                    min_penality = y_count + n_count
                    earliest_hour = i

        return earliest_hour
