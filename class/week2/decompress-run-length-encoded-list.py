class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decomp = []
        for i in range(len(nums)//2):
            temp = [nums[2*i], nums[2*i + 1]]
            decomp += [temp[1]]*temp[0]
        
        return decomp
