class FrequencyTracker:

    def __init__(self):
        self.freq_dict = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq[self.freq_dict[number]] = max(0,self.freq[self.freq_dict[number]]-1)
        self.freq_dict[number] += 1
        self.freq[self.freq_dict[number]] += 1

    def deleteOne(self, number: int) -> None:
        self.freq[self.freq_dict[number]] = max(0,self.freq[self.freq_dict[number]]-1)
        self.freq_dict[number]=max(self.freq_dict[number]-1,0)
        self.freq[self.freq_dict[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        # print(self.freq)
        # print(self.freq_dict)
        return self.freq[frequency] != 0