class RecentCounter:

    def __init__(self):
        self.queue = []
        self.i = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue and self.queue[self.i] < t - 3000:
            self.i += 1
        
        return len(self.queue)-self.i


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)